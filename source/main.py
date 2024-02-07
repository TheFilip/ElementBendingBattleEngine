#newMain
import random, math, time, sys, requests, importlib.util
from statistics import mean
from scipy.interpolate import make_interp_spline
from collections import Counter
from combat import *
from matchInfo import *
random.seed(int(seed), version=2)
#####################################################################Database
if False:
    # GitHub URL
    github_url = 'https://raw.githubusercontent.com/TheFilip/ElementBendingBattleEngine/main/source/characterDB.py'

    # Fetch the content of the file
    response = requests.get(github_url)
    character_db_code = response.text

    # Create a temporary module
    temp_module_name = 'temp_characterDB'
    spec = importlib.util.spec_from_loader(temp_module_name, loader=None)
    temp_module = importlib.util.module_from_spec(spec)

    # Execute the code from the GitHub file in the temporary module
    exec(character_db_code, temp_module.__dict__)

    # Add the temporary module to sys.modules
    sys.modules[temp_module_name] = temp_module

    from temp_characterDB import *
else:
    # Local use of character Database
    from characterDB import *
#####################################################################Database

# Seting default for emote conversations to false
defaultEmoticonConversations = False

# Setting use of emotes when printing players' names to True
useEmotes = True

# Setting potential MVP list and an empty list for players in turn
potMVPs = []
turnPlayers = []

# Timer for rounds
currentRoundTime = 0
totalTimePassed = 0

# Setting defaults for rounds
resultsList = []

# This counts time and prints out the time
timerActive = True

# If activates, will compare current round time to maxRoundTime, then stop the round if over
maxRoundTime = 1 # In Minutes
timerRunOutActive = True
timerRanOut = False

# Count and Print time
def roundTimeAdd():
    if timerActive == True:
        global currentRoundTime
        currentRoundTime += random.randrange(1,4)+random.randrange(1,4)
        if random.randrange(1,10)<=8:
            print("---")
            #print(str(currentRoundTime)+" minutes has passed")
            print("Round Time: "+str(currentRoundTime)+" minutes")
            print("---")


# Chance for a player to be singled out to say they need to be substituted
allowPlayerSubstitution = False
def playerSubstitute(listOfPlayers):
    if allowPlayerSubstitution:
        subChance = 10#/100
        while random.randint(1,100)<=subChance:
            player = random.choice(listOfPlayers)
            print(player.name,"should be substituted")
            input()


# Count how many times players appear in list (potMVP) and sum up with their successful Hit and knockouted Amount
def count_items(input_list):
    # Convert objects to tuples with additional attributes for hashability
    input_tuples = [(item.name, item.successfulHits, item.knockedoutAmount) for sublist in input_list for item in sublist]

    # Use Counter to count the occurrences of each item
    item_counts = Counter(input_tuples)

    # Sort items by count in descending order
    sorted_items = sorted(item_counts.items(), key=lambda x: sum(x[0][1:]) + x[1], reverse=True)

    # Print the result
    print("-Potential MVPs-")
    for item, count in sorted_items:
        total_count = sum(item[1:]) + count
        print(f"{item[0]}: knocked out {item[2]} - successful hits {item[1]}")
        #print(f"{item[0]}")

# Displays selected team roster
def displayRoster(team):
    print(f"----------\n{team.name} Roster")
    for i in team.roster:
        if useEmotes:
            print(f"{random.choice(emoticonsFaces)} {i.name} the {i.element}bending {i.role}")
        else:
            print(f"{i.name} the {i.element}bending {i.role}")
    print(f"----------")

def printRosterStats(team):
    print("\n\n"+team+"\n----")
    for i in team:
        print(i.name+": knocked out:",i.knockedoutAmount," - successful hits:",i.successfulHits)
        i.knockedoutAmount = 0
        i.successfulHits = 0

# Class to create a team
class team:
    def __init__(self,name,roster):
        self.name = name
        self.roster = roster
        self.rosterBackup = roster[:]
        self.winNumber = 0
        self.loseNumber = 0

    # Refreshes all players health
    def reset_health(self):
        for player in self.roster:
            player.health = player.healthBackup

    # Used to reset the roster after removing everyone
    def roster_backup(self):
        self.roster = self.rosterBackup[:]
    
    def resetWinLose(self):
        self.winNumber = 0
        self.loseNumber = 0
    
def teamWinning(team1,team2):
    if len(team1.roster) > len(team2.roster):
        print(f"{team1.name} wins the round!")
        team1.winNumber+=1
        team2.loseNumber+=1
    elif len(team1.roster) < len(team2.roster):
        print(f"{team2.name} wins the round!")
        team1.loseNumber+=1
        team2.winNumber+=1
    else:
        print("The round is a draw!")


# Main Match Function
def runRound(homeTeam,awayTeam,setEmoticonConversations,):
    global totalRoundsPassed, totalTimePassed, currentRoundTime
    timerRanOut = False
    currentRoundTime = 0

    print("----- NEW MATCH ROUND STARTS -----")
    displayRoster(homeTeam)
    displayRoster(awayTeam)

    # Check if length of both teams is above 0
    while homeTeam.roster and awayTeam.roster and not timerRanOut:
        #time.sleep(1)

        # Clear and reset turn players to include all players currently in play
        turnPlayers = homeTeam.roster+awayTeam.roster

        # For every player in play, run their turn choice
        for i in homeTeam.roster:
            i.turnChoice(awayTeam.roster)
        for i in awayTeam.roster:
            i.turnChoice(homeTeam.roster)

        # Sort players by initiative
        turnPlayers.sort(key=lambda x: x.initiative, reverse=True)
        
        # Check if it's start of round
        if currentRoundTime == 0:
            pass
        else:
            # Display team rosters and their current zone location
            if random.randrange(1,10) <= 5:
                print("----------")
                print(homeTeam.name)
                for i in homeTeam.roster:
                    printCurrentZone(i)
                print("-----")
                print(awayTeam.name)
                for i in awayTeam.roster:
                    printCurrentZone(i)
                print("----------")

        # Action per turn for each player
        for i in turnPlayers:

            # Check if current player's target is still in play
            if not homeTeam.roster or not awayTeam.roster:
                break
            if i.target not in turnPlayers:
                # If not, check what team current player is in and assign new target
                if i in homeTeam.roster:
                    i.chooseRandomOpponent(awayTeam.roster)
                if i in awayTeam.roster:
                    i.chooseRandomOpponent(homeTeam.roster)

            # Run compareStats combat
            compareStats(i,i.target,setEmoticonConversations)

            # Check if target's health is 0 or less, if so remove from that team's roster and increase current player's knocked out count
            if i.target.health<=0:
                i.knockedoutAmount += 1
                turnPlayers.remove(i.target)
                if i.target in homeTeam.roster:
                    homeTeam.roster.remove(i.target)
                if i.target in awayTeam.roster:
                    awayTeam.roster.remove(i.target)

            # Remove knocked-out player from the list of potential targets for other players
            for team_ in [homeTeam, awayTeam]:
                team_.roster = [player for player in team_.roster if player.health > 0]
            
        # Run round timer function
        roundTimeAdd()
        
        # Check if out of time for the round, if so end match
        if timerRunOutActive:
            if currentRoundTime >= maxRoundTime:
                timerRanOut = True
                print("Out Of Time!")
        

    else:
        # Run after round finishes
        print("----- ROUND FINISH -----")
        print("This round lasted",str(currentRoundTime),"minutes")
        totalTimePassed += currentRoundTime
        printLeftOverPlayers(turnPlayers)
        teamWinning(homeTeam,awayTeam)  
        potMVPs.append(turnPlayers)
        
# Print players left in list
def printLeftOverPlayers(list):
            print("-Players Left In Round-")
            for i, winner in enumerate(list):
                print(winner.name, end=', ' if i < len(list) - 1 else '\n')
            print()

def playerStats(team_):
    print("\n\n"+team_.name+"\n----")
    for i in team_.rosterBackup:
        print(i.name+": knocked out:",i.knockedoutAmount," - successful hits:",i.successfulHits)
        i.knockedoutAmount = 0
        i.successfulHits = 0



# Print out at the end of all matches
def endOfMatchDisplay(homeTeam,awayTeam):
    print("\n-----------\nMatch Time: "+str(totalTimePassed)+" minutes")
    for team_ in [homeTeam, awayTeam]:
        print(f"{team_.name}:{team_.winNumber}")
    count_items(potMVPs)
    playerStats(homeTeam)
    playerStats(awayTeam)


# Main Function: Handles all code of running match per amounts wanted
def mainMatchRun(team1Name,team1Players,team2Name,team2Players,amountOfRounds=1,setEmoticonConversations=defaultEmoticonConversations,timerActivation=False,maxTurnTime=0):
    team1Players = [player for player in team1Players if player is not None]
    team2Players = [player for player in team2Players if player is not None]

    # Adjust amount of runs and how many rounds needed to win
    runs = matchesN*amountOfRounds
    rounds_to_win = math.ceil(runs / 2)

    # Set home and away teams with names and rosters
    homeTeam = team(team1Name,team1Players)
    awayTeam = team(team2Name,team2Players)
    
    # Blank Slate
    def init():
        global potMVPs,roundsPassed,totalRoundsPassed,totalTimePassed,roundResults,resultsList

        # TODO: make a seperate function to startup and clean this up

        # Set home and away teams with names and rosters
        for team_ in [homeTeam, awayTeam]:
            team_ = team(team1Name,team1Players)
            team_.resetWinLose()

        potMVPs = []
        roundResults = []
        resultsList = []
        totalTimePassed = 0
        for player in team1Players + team2Players:
            player.reset()
    init()

    # Run rounds per amount in runs
    for i in range(runs):       
        # For every team, reset roster and player health
        for team_ in [homeTeam, awayTeam]:
            team_.roster_backup()
            team_.reset_health()

        global timerRunOutActive, maxRoundTime
        maxRoundTime = maxTurnTime
        timerRunOutActive = timerActivation
        # Run round
        runRound(homeTeam,awayTeam,False)

        # If team won more that half, end
        if homeTeam.winNumber >= rounds_to_win or awayTeam.winNumber >= rounds_to_win:
            break
    if homeTeam.winNumber == 0 and awayTeam.winNumber == 0:
        for team_ in [homeTeam, awayTeam]:
            team_.roster_backup()
            team_.reset_health()
        timerRunOutActive = False
        print("--- Tie Breaker ---")
        runRound(homeTeam,awayTeam,False)

    endOfMatchDisplay(homeTeam,awayTeam)


# Run Main
#mainMatchRun("Blue",[Yuka,Asuka],"Red",[Renji,Kaito],100)