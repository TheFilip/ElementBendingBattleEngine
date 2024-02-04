#custom game engine for Avatar Legends: Onyx Control

#idea; attack, defend, observe & strategize
#stats from 1-100, average % compared to others in program
#team stat too, sum all and divide by 150(?) and thats a stat multiplier before comparesent.
#picks random opponent, each needs to be hit 9 times to be knocked off. (time limit?)
import random, sys, matplotlib.pyplot as plt, numpy as np
import plotly.express as px
import pandas as pd
from statistics import mean
from scipy.interpolate import make_interp_spline
from collections import Counter
from combat import *
from matchInfo import *


import sys
import requests
import importlib.util






#####################################################################Database
if True:
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


















random.seed(int(seed), version=2)

baseHitTarget = 3
elementList = ["Earth","Fire","Water"]

global RedTeam,BlueTeam



xP = []
yPP = []
yP = 0



#RedTeam = [Yuka,Asuka,Mei]
#BlueTeam = [JinHo,Kaito,Renji]





global t1W,t2W
t1W=0
t2W=0






winningTeam = "winner"
winningName = "x"
defaultEmoticonConversations = False
setEmoticonConversations = False


roundsPassed = 0
totalRoundsPassed = 0
resultsList = []










#generate plot ideas
plotGen = True
useEmotes = True
knockoutAmounts = []





totalHP1 = 0
totalHP2 = 0
potMVPs = []
turnPlayers = []




#timer for rounds
maxRoundTime = 7
currentRoundTime = 0
totalTimePassed = 0
timerActive = True
timerRunOutActive = False

def roundTimeAdd():
    if timerActive == True:
        global currentRoundTime
        currentRoundTime += random.randrange(1,6)+random.randrange(1,6)
        if random.randrange(1,10)<=8:
            print("---")
            #print(str(currentRoundTime)+" minutes has passed")
            print("Round Time: "+str(currentRoundTime)+" minutes")
            print("---")
        
    





def playerSubstitute(listOfPlayers):
    if False: #activate Substitues
        subChance = 10#/100
        while random.randint(1,100)<=subChance:
            player = random.choice(listOfPlayers)
            print(player.name,"should be substituted")
            input()









def count_items(input_list):
    # Convert objects to tuples with additional attributes for hashability
    input_tuples = [(item.name, item.successfulHits, item.knockedoutAmount) for sublist in input_list for item in sublist]

    # Use Counter to count the occurrences of each item
    item_counts = Counter(input_tuples)

    # Sort items by count in descending order
    sorted_items = sorted(item_counts.items(), key=lambda x: sum(x[0][1:]) + x[1], reverse=True)

    # Print the result
    for item, count in sorted_items:
        total_count = sum(item[1:]) + count
        print(f"{item[0]}: knocked out {item[2]} - successful hits {item[1]}")
        #print(f"{item[0]}")

























def match(team1,team2,setEmoticonConversations):
    global teamA, teamB
    global totalHP1, totalHP2, totalRoundsPassed, totalTimePassed
    global winningTeam,winningName
    roundsPassed = 0
    roundResults = []
    playerSubstitute(team1 + team2)



    print("----------\n"+firstTeamName)
    for i in team1:
        if useEmotes:
            if i.health == innerZone:
                print(random.choice(emoticonsFaces),i.name,"the",i.element+"bending "+i.role)
            elif i.health == middleZone:
                print(random.choice(emoticonsFaces),i.name,"the",i.element+"bending "+i.role)
            elif i.health == outsideZone:
                print(random.choice(emoticonsFaces),i.name,"the",i.element+"bending "+i.role)
        else:
            if i.health == innerZone:
                print(i.name,"the",i.element+"bending "+i.role)
            elif i.health == middleZone:
                print(i.name,"the",i.element+"bending "+i.role)
            elif i.health == outsideZone:
                print(i.name,"the",i.element+"bending "+i.role)
    #print out all players for second team
    print("-----\n"+secondTeamName)
    for i in team2:
        if useEmotes:
            if i.health == innerZone:
                print(random.choice(emoticonsFaces),i.name,"the",i.element+"bending "+i.role)
            elif i.health == middleZone:
                print(random.choice(emoticonsFaces),i.name,"the",i.element+"bending "+i.role)
            elif i.health == outsideZone:
                print(random.choice(emoticonsFaces),i.name,"the",i.element+"bending "+i.role)
        else:
            if i.health == innerZone:
                print(i.name,"the",i.element+"bending "+i.role)
            elif i.health == middleZone:
                print(i.name,"the",i.element+"bending "+i.role)
            elif i.health == outsideZone:
                print(i.name,"the",i.element+"bending "+i.role)
    print("----------")
    #turnPlayers.sort(key=lambda x: x.initiative, reverse=True)
                        #run combat per player for each team
    

    #t1W=0
    #t2W=0

    print("----- NEW MATCH ROUND STARTS -----")
    print("----------\n"+firstTeamName)
    for i in team1:
        if i.health == innerZone:
            print(i.name,"the",i.element+"bender - Inner Zone")
        elif i.health == middleZone:
            print(i.name,"the",i.element+"bender - Middle Zone")
        elif i.health == outsideZone:
            print(i.name,"the",i.element+"bender - Outside Zone")
    #print out all players for second team
    print("-----\n"+secondTeamName)
    for i in team2:
        if i.health == innerZone:
            print(i.name,"the",i.element+"bender - Inner Zone")
        elif i.health == middleZone:
            print(i.name,"the",i.element+"bender - Middle Zone")
        elif i.health == outsideZone:
            print(i.name,"the",i.element+"bender - Outside Zone")
    print("----------")





    global currentRoundTime
    currentRoundTime = 0 #timer resets to 0 at start of round





    while len(team1)>0 and len(team2)>0:
        global yP, xP, yPP
        totalHP1 = 0
        totalHP2 = 0
        yPP.append(yP)
        yP = 0

        for i in team1:
            if i.health<0 or i.health==0:
                #print("-----")
                #print(i.name,"from",firstTeamName,"has been knocked out!")
                team1.remove(i)
                yP-=1
                
            else:
                totalHP1 += i.health
        for i in team2:
            if i.health<0 or i.health==0:
                #print("-----")
                #print(i.name,"from",secondTeamName,"has been knocked out!")
                team2.remove(i)
                yP+=1
            else:
                totalHP2 += i.health





            
        #yP+=(totalHP1-totalHP2) ############################# WORKING HERE ON THIS ALGO

        
        xP.append(totalRoundsPassed)


        



        turnPlayers = []
        turnPlayers = team1 + team2
        #turnPlayers.clear()
        #turnPlayers.insert(team1)
        #turnPlayers.insert(team2)
        #PRINT HEALTH OF PLAYERS AT START OF ROUND
        #print("----------")



        






        if len(team1) == 0:
            break
        else:
            if len(team2) == 0:
                break
            else:
                
                roundsPassed += 1
                totalRoundsPassed += 1
        
                #print("----- Turn",roundsPassed,"-----")

                for i in team1:
                    i.turnChoice(team2)
                for i in team2:
                    i.turnChoice(team1)




                




                #print out all players for first team
                if True:
                    if currentRoundTime == 0:
                        pass
                    else:
                        if random.randrange(1,100) <= 40:
                            print("----------")
                            print(firstTeamName)
                            for i in team1:
                                if i.health == innerZone:
                                    print(i.name,"the",i.element+"bender - Inner Zone")
                                elif i.health == middleZone:
                                    print(i.name,"the",i.element+"bender - Middle Zone")
                                elif i.health == outsideZone:
                                    print(i.name,"the",i.element+"bender - Outside Zone")
                            print("-----")
                            #print out all players for second team
                            print(secondTeamName)
                            for i in team2:
                                if i.health == innerZone:
                                    print(i.name,"the",i.element+"bender - Inner Zone")
                                elif i.health == middleZone:
                                    print(i.name,"the",i.element+"bender - Middle Zone")
                                elif i.health == outsideZone:
                                    print(i.name,"the",i.element+"bender - Outside Zone")
                            print("----------")
                            turnPlayers.sort(key=lambda x: x.initiative, reverse=True)
                            #run combat per player for each team





                #player selects a opponent to target
                for i in turnPlayers:
                    if not team1:
                        pass
                    elif not team2:
                        pass
                    else:
                        
                        #print(i.name,"- currently in zone",i.health) #print out what zones the player is on.
                        if not team1 and not team2:
                            pass
                        else:
                            if i in team1: ########## KEEP EYE ON THIS
                                i.chooseRandomOpponent(team2)
                            else:
                                i.chooseRandomOpponent(team1)

                        #combat per player
                        compareStats(i,i.target,setEmoticonConversations)
                        if i.target.health<0 or i.target.health == 0:
                            if i.target in team1:
                                #print(i.target.name,"from",firstTeamName,"has been knocked out!")
                                team1.remove(i.target)
                                turnPlayers.remove(i.target)
                                yP-=1
                            if i.target in team2:
                                #print(i.target.name,"from",secondTeamName,"has been knocked out!")
                                team2.remove(i.target)
                                turnPlayers.remove(i.target)
                                yP+=1 
                            i.knockedoutAmount += 1






                #for i in team1:
                    #print("-")
                    #print(i.name,"-",i.health)
                    #compareStats(i,i.target)
                #for i in team2:
                    #print("-")
                    #print(i.name,"-",i.health)
                    #compareStats(i,i.target)
                if timerRunOutActive:
                    if currentRoundTime >= maxRoundTime: #if the current time that passed in round is more than maximum allowed, end round.
                        print("Time ran out!")
                        break
                else:
                    roundTimeAdd()










        #input() #### REMOVE FOR FAST GEN
        
        




    winners = []

    print("----- ROUND FINISH -----")
    print("This round lasted",str(currentRoundTime),"minutes")


    def printWinners():
        print("-Players Left In Round-")
        for i, winner in enumerate(winners):
            print(winner.name, end=', ' if i < len(winners) - 1 else '\n')
        print()
        #print(len(team1),":",len(team2))

    if len(team1)>len(team2):
        global t1W,t2W,winningTeam,winningName
        print(firstTeamName,"Wins!")
        for i in team1:
            winners.append(i)
            #knockoutAmounts.extend((i.name,i.knockedoutAmount))
        printWinners()
        t1W +=1
    elif len(team1)<len(team2):
        print(secondTeamName,"Wins!")
        for i in team2:
            winners.append(i)
            #knockoutAmounts.extend((i.name,i.knockedoutAmount))

        printWinners()
        t2W +=1
    else:
        print("Draw!")
    roundResults = [(len(team1),len(team2))]
    totalTimePassed += currentRoundTime
    potMVPs.append(winners)


    #for i in potMVPs:
        #knockoutAmounts.append((i.name,":",i.knockedoutAmount))




    resultsList.append(roundResults)

    #print("----- ROUND FINISH -----")



#FIGHT HAPPENS
def phase1(aTeamName,a,bTeamName,b,amountOfRounds=1,setEmoticonConversations=defaultEmoticonConversations):
    a = [player for player in a if player is not None]
    b = [player for player in b if player is not None]
    roundsN = amountOfRounds
    runs = matchesN*roundsN
    print("seed:",seed)
    global winningTeam,winningName, firstTeamName, secondTeamName, displayStoryText
    displayStoryText = True

    def init():
        global t1W,t2W,potMVPs,roundsPassed,totalRoundsPassed,totalTimePassed,roundResults,resultsList
        t1W = 0
        t2W = 0
        potMVPs = []
        roundResults = []
        resultsList = []
        roundsPassed = 0
        totalRoundsPassed = 0
        totalTimePassed = 0
    init()

    firstTeamName = aTeamName
    secondTeamName = bTeamName
    #knockoutAmounts = []


    #for i in both teams
        #append playermove list with "Special move" so everyone has 1 for the whole match. Or maybe even roll a chance and if > chance then they get special move.




    if plotGen == True:
        generateText(random.choice(a+b),random.choice(a+b),7)
        for i in range(4):
            if random.randint(1,100) <= chancesOfDescription:
                generateText(random.choice(a+b),random.choice(a+b),None)

    targetToWin = (roundsN+1)/2
    for i in range(runs):
        if t1W == targetToWin or t2W == targetToWin:
            break
        for u in a:
            u.health = baseHitTarget
        for u in b:
            u.health = baseHitTarget
        teamA = a.copy()
        teamB = b.copy()
        match(teamA,teamB,setEmoticonConversations)

        if len(teamA) == len(teamB): #IF A DRAW HAPPENS #not teamA and not teamB
            teamA = a.copy()
            teamB = b.copy()
            elementChosen = random.choice(elementList)
            for p in teamA:
                if p.element != elementChosen:
                    teamA.remove(p)
            for p in teamB:
                if p.element != elementChosen:
                    teamB.remove(p)
            print("A draw has happened!",elementChosen+"benders are going to battle this one out!")
            match(teamA,teamB,setEmoticonConversations)






    yPPAverage = [sum(yPP[:i+1]) / (i+1) for i in range(len(yPP))]


    #yPPAverage = []########################### ##### WORKING ON HERE to get average and show a second plot of average throughout the match
    #for i in yPP:
    #    tempi = sum(yPP[0:i+1]) / len(yPP[0:i+1])

    #    yPPAverage.append(tempi)




    if True:
        print("MATCH FINISH!")


        if plotGen == True:
            generateText(random.choice(a+b),random.choice(a+b),7)
            for i in range(4):
                if random.randint(1,100) <= chancesOfDescription:
                    generateText(random.choice(a+b),random.choice(a+b),None)


        
        print(firstTeamName,":",secondTeamName)
        print("Match Time: "+str(totalTimePassed)+" minutes")
        print((t1W),":",((t2W)))
        
        print(((t1W/(t1W+t2W))*100),"win %:win %",(((t2W)/(t1W+t2W)))*100)
        
        print("-Potential MVPs-")
        count_items(potMVPs)
        #print("Potential MVPs:",potMVPs)
        teamA = a.copy()
        teamB = b.copy()
        print("\n\n"+aTeamName+"\n----")
        for i in teamA:
            print(i.name+": knocked out:",i.knockedoutAmount," - successful hits:",i.successfulHits)
            i.knockedoutAmount = 0
            i.successfulHits = 0
        print("\n"+bTeamName+"\n----")
        for i in teamB:
            print(i.name+": knocked out:",i.knockedoutAmount," - successful hits:",i.successfulHits)
            i.knockedoutAmount = 0
            i.successfulHits = 0
        




        #for i in teamA and teamB: ########################################WORK ON THIS TOO
            #knockoutAmounts.extend((i.name,i.knockedoutAmount))
        #print(knockoutAmounts)


        print("----\nRound Results:",resultsList)
        

        #MVPRanking = []
        #for i in potMVPs:
        #    MVPRanking

        
        if t1W>t2W:
            winningName = "A"
        elif t2W>t1W:
            winningName = "B"








        #PLOTTING PLOt
        plt.figure(figsize=(10, 6))


        #x_smooth = np.linspace(min(xP), max(xP), 100)  # Create a smoother x-axis
        #array1_smooth = make_interp_spline(xP, yPP)(x_smooth)
        #array2_smooth = make_interp_spline(xP, yPPAverage)(x_smooth)





        
        #plt.plot(xP, yPP,marker='o',markersize=3)
        plt.plot(xP, yPPAverage)


        #plt.plot(x_smooth, array1_smooth)
        #plt.plot(x_smooth, array2_smooth)

        # naming the x axis
        plt.xlabel('Rounds')
        # naming the y axis
        plt.ylabel('Advantage')


        plt.annotate(f'{yPPAverage[-1]:.2f}', (xP[-1], yPPAverage[-1]), textcoords="offset points", xytext=(0, 10), ha='center')




        if matchesN == 1:
            plt.xticks(xP)
        # giving a title to my graph
        plt.title('Advantage Plot')
        


        # function to show the plot
        #plt.show()
    if t1W>t2W:
        winningName = "A"
    elif t2W>t1W:
        winningName = "B"
    winningTeam = winningName





#output stats and generate scatter radar graphs for all players
def outputStats(a):  
    for i in a:
        mainTitle = f"{i.name} - {i.element} {i.role}"
        df = pd.DataFrame(dict(
            #r=[i.attackStat, i.blockStat, i.bendingStat, i.maneuverStat, i.observeStat],
            r=[i.bendingStat, i.attackStat, i.observeStat, i.maneuverStat, i.blockStat],
            #theta=['Offense', 'Defense', 'Bending', 'Maneuver', 'Vision'],
            theta=['Bending', 'Offense', 'Vision', 'Maneuver', 'Defense'],
        ))
        fig = px.line_polar(df, r='r', theta='theta', line_close=True)
        fig.update_polars(
            radialaxis_tickvals=[0, 20, 40, 60, 80, 100],
            radialaxis_tickmode="array",
            radialaxis_range=[0, 100],
        )
        fig.update_layout(
            font=dict(size=20),
            title=mainTitle,
            title_x=0.5,
        )
        # Add fill to the polar area
        fig.update_traces(fill='toself')  # Added fill='toself'
        fig.show()

    for i in a:
        print(i.name,"-","Offense:",i.attackStat,"Defense:",i.blockStat,"Bending:",i.bendingStat,"Maneuver:",i.maneuverStat,"Vision:",i.observeStat)






def createOwnTeam():
    
    global homeTeam,awayTeam, balance
    balance = 150
    #create own random team\
    print(balance)
    r1 = random.choice(playerList)
    r2 = random.choice(playerList)
    r3 = random.choice(playerList)
    print(r1.name,"- Role:",r1.role,"~",r1.value,"\n"+r2.name,"- Role:",r2.role,"~",r2.value,"\n"+r3.name,"- Role:",r3.role,"~",r3.value)
    p1 = input("Choose Player 1: ")
    if p1 == r1.name:
        p1 = r1
        balance -= r1.value
    elif p1 == r2.name:
        p1 = r2
        balance -= r2.value
    elif p1 == r3.name:
        p1 = r3
        balance -= r3.value
    print(balance)
    r1 = random.choice(playerList)
    r2 = random.choice(playerList)
    r3 = random.choice(playerList)
    print(r1.name,"- Role:",r1.role,"~",r1.value,"\n"+r2.name,"- Role:",r2.role,"~",r2.value,"\n"+r3.name,"- Role:",r3.role,"~",r3.value)
    p2 = input("Choose Player 2: ")
    if p2 == r1.name:
        p2 = r1
        balance -= r1.value
    elif p2 == r2.name:
        p2 = r2
        balance -= r2.value
    elif p2 == r3.name:
        p2 = r3
        balance -= r3.value
    print(balance)
    r1 = random.choice(playerList)
    r2 = random.choice(playerList)
    r3 = random.choice(playerList)
    print(r1.name,"- Role:",r1.role,"~",r1.value,"\n"+r2.name,"- Role:",r2.role,"~",r2.value,"\n"+r3.name,"- Role:",r3.role,"~",r3.value)
    p3 = input("Choose Player 3: ")
    if p3 == r1.name:
        p3 = r1
        balance -= r1.value
    elif p3 == r2.name:
        p3 = r2
        balance -= r2.value
    elif p3 == r3.name:
        p3 = r3
        balance -= r3.value
    homeTeam=[p1,p2,p3]
    awayTeam = [random.choice(playerList),random.choice(playerList),random.choice(playerList)]