import random
from matchInfo import *

random.seed(int(seed), version=2)

chancesOfDescription = 15#65#/100%
global dialogAmount
dialogAmount = 0
dialogAmountTarget = 55

dialogPlacementRate = 7#/10  Needs to roll same or less to succeed

def printDialog(player1,player2):
    if random.randint(1,10) <= dialogPlacementRate:
        generateText(player1,player2,random.choice(["Monologue","Conversation"]))
        while round(random.randint(1,10)/2) >= dialogPlacementRate:
            generateText(player1,player2,random.choice(["Monologue","Conversation","Conversation"]))







#displayStoryText = True
typeOfText = "emoticon" #emoticon/text



        
#zone thresholds
#print(i.name,"the",i.element+"bender - zone",i.health)
innerZone = baseHitTarget
middleZone = round(baseHitTarget/2)
outsideZone = 1






storeBestPlaysList = []


damageBeingTaken = 0

moveSuccessChance = 90
#Critical Hits
critRate = 100

criticalHitText = random.choice(["👹", "👺", "👻", "👽", "👾", "🤖", "🐝", "🐉", "🦬"])
# ["Flow has been awakened for this attack which causes opponent to get knocked back further!"]
# ["👹", "👺", "👻", "👽", "👾", "🤖"]

critsActive = True
criticalAttackSuccessful = False
strongMoveSuccessful = False

def criticalAttack(damageBeingTaken, player):
    if player.movePower >= (75/modifier): #15
        # global damageBeingTaken
        damageBeingTaken += 1
        print(f"Flow Awakened to strengthen attack {criticalHitText}")
        return damageBeingTaken


def printCurrentZone(player):
    if player.health == outsideZone:
        print(f"{player.name} currently in - Outside Zone")
    elif player.health <= middleZone:
        print(f"{player.name} currently in - Middle Zone")
    elif player.health <= innerZone:
        print(f"{player.name} currently in - Inner Zone")




def storeBestPlays(i,opponenti,strongMoveSuccessful,criticalAttackSuccessful,time):
    global storeBestPlaysList
    if strongMoveSuccessful:
        storeBestPlaysList.append(random.choice([
    f"At the {time} minute, {i.name} from the {i.zoneName} successfully used the '{i.moveChoice[0]}' technique. The strong hit knocked {opponenti.name} straight out of the arena!",
    f"At the {time} minute mark, {i.name} executed the '{i.moveChoice[0]}' technique flawlessly. The forceful impact sent {opponenti.name} flying out of the arena!",
    f"During the {time} minute mark, {i.name} from the {i.zoneName} deftly performed the '{i.moveChoice[0]}' move. {opponenti.name} was sent tumbling out of the arena."
]))
    elif criticalAttackSuccessful:
        storeBestPlaysList.append(random.choice([
    f"At the {time} minute, {i.name} from the {i.zoneName} successfully used the '{i.moveChoice[0]}' technique. Critically knocking {opponenti.name} straight out of the arena!",
    f"At {time} minutes, {i.name} from the {i.zoneName} unleashed a devastating '{i.moveChoice[0]}' technique. The impact was so powerful that {opponenti.name} was hurled out of the arena!",
    f"During the {time} minute mark, {i.name} executed a flawless '{i.moveChoice[0]}' move. The force sent {opponenti.name} crashing out of the arena."
]))





def compareStats(player1,player2,time,displayStoryText=False):
    attackSuccessfulText = False
    criticalAttackSuccessful = False
    strongMoveSuccessful = False

    print("-")
    if True:
        #print("-")

        printCurrentZone(player1)
    #emoticon reactions set, check if to print at start or end
    dialogPlacement = random.choice(["start","both","end"])
    if displayStoryText:
        if dialogPlacement == "start" or dialogPlacement == "both":
            printDialog(player1,player2)

    # Check if player's move of choice has a failure adjustment, if so take away from roll
    if len(player1.moveChoice) >= 3:
        failureNumber = random.randint(1,100) - player1.moveChoice[2]
    else:
        failureNumber = random.randint(1,100)

    # Check if technique fails
    if failureNumber > moveSuccessChance:
        print(f"{player1.name}'s '{player1.moveChoice[0]}' technique has failed")
    else:


        #Player Choosing Action for Turn


        # TODO: MAKE SO BLOCK DOESNT HURT - INSTEAD BLOCKS ATTACK + BENDING , OBSERVE DOESN'T HURT - BLOCKS MANEUVER + BENDING

        #Player Choice being Attack
            if player1.moveChoice[1] == "attack":
                #same as user
                if player2.moveChoice[1] == "attack":
                    print(f"{player1.name} and {player2.name} enter a offensive showdown")
                    if player1.movePower > player2.movePower:
                        attackSuccessfulText = True
                        #print(player1.name+"'s '"+player1.element,player1.moveChoice[0]+"' technique overwhelms "+player2.name)
                        print(f"{player1.name}'s {player1.element} '{player1.moveChoice[0]}' technique overwhelms {player2.name}")
                    else:
                        print(f"{player1.name} tries to hit {player2.name} with their {player1.element} '{player1.moveChoice[0]}' technique but isn't successful")
                #user beats
                elif player2.moveChoice[1] == "observe" or player2.moveChoice[1] == "bending":
                    attackSuccessfulText = True
                    if player2.moveChoice[1] == "observe":
                        print(f"{player1.name} manages to hit {player2.name} with their {player1.element} '{player1.moveChoice[0]}' technique while {player2.name} is distracted")
                    else:
                        print(f"{player1.name}'s offensive '{player1.moveChoice[0]}' technique overwhelms {player2.name}'s inferior bending shots")
                #beats user
                elif player2.moveChoice[1] == "block" or player2.moveChoice[1] == "maneuver":
                    if player2.moveChoice[1] == "block":
                        print(f"{player2.name} successfully deflects {player1.name}'s {player1.element} '{player1.moveChoice[0]}' technique")
                    else:
                        print(f"{player2.name} outmaneuvers {player1.name}'s {player1.element} '{player1.moveChoice[0]}' technique")

        #Player Choice being Block
            elif player1.moveChoice[1] == "block":
                #same as user
                if player2.moveChoice[1] == "block":
                    print(f"{player1.name} and {player2.name} both get into defensive positions")
                    if player1.movePower > player2.movePower:
                        print(f"{player2.name}'s {player2.element} {player1.moveChoice[0]}' blocking technique was too weak for {player1.name}'s {player1.element} bending attacks")
                        attackSuccessfulText = True
                    else:
                        print(f"{player2.name} manages to block {player1.name}'s {player1.element} bending attacks")
                #user beats
                elif player2.moveChoice[1] == "attack" or player2.moveChoice[1] == "observe":# or player2.moveChoice[1] == "bending":
                    attackSuccessfulText = True
                    if player2.moveChoice[1] == "attack":
                        print(f"{player1.name}'s '{player1.element} {player1.moveChoice[0]}' technique successfully counters {player2.name}'s {player2.element} attacks")
                    else:
                        print(f"{player1.name} manages to successfully hit {player2.name} as {player1.name}'s '{player1.element} {player1.moveChoice[0]}' technique was too difficult to analyse")
                #beats user
                elif player2.moveChoice[1] == "maneuver" or player2.moveChoice[1] == "bending":
                    if player2.moveChoice[1] == "maneuver":
                        print(f"{player2.name} outmaneuvers {player1.name}'s defensive moves")
                    else:
                        print(f"{player1.name}'s defensive moves aren't enough to break {player2.name}'s bending shots")

            #Player Choice being Observe
            elif player1.moveChoice[1] == "observe":
                #same as user
                if player2.moveChoice[1] == "observe":
                    print(f"{player1.name} and {player2.name} carefully analyse the other's attacks")
                    if player1.movePower > player2.movePower:
                        print(f"{player1.name} gets a clean {player1.element} bending hit against {player2.name}")
                        attackSuccessfulText = True
                    else:
                        print(f"{player1.name}'s {player1.element} attacks were too easy for {player2.name} to read")
                #user beats
                elif player2.moveChoice[1] == "bending" or player2.moveChoice[1] == "maneuver":# or player2.moveChoice[1] == "block":
                    attackSuccessfulText = True
                    if player2.moveChoice[1] == "bending":
                        print(f"{player1.name} successfully uses their '{player1.moveChoice[0]}' technique to analyse {player2.name}'s {player2.element} bending habits and sneaks in a hit")
                    else:
                        print(f"{player1.name} successfully uses their '{player1.moveChoice[0]}' technique to analyse {player2.name}'s movements and predicts their shots to hit {player2.name}")
                #beats user
                elif player2.moveChoice[1] == "attack" or player2.moveChoice[1] == "block":
                    if player2.moveChoice[1] == "attack":
                        print(f"{player2.name}'s attacks are too difficult for {player1.name} to analyse")
                    else:
                        print(f"{player2.name}'s defending moves are too difficult for {player1.name} to analyse")

            #Player Choice being Maneuver
            elif player1.moveChoice[1] == "maneuver":
                #same as user
                if player2.moveChoice[1] == "maneuver":
                    print(f"{player1.name} and {player2.name} are both attempting to secure an advantageous position")
                    if player1.movePower > player2.movePower:
                        print(f"{player1.name} skillfully uses their '{player1.moveChoice[0]}' technique and lands a precise {player1.element} attack against {player2.name}")
                        attackSuccessfulText = True
                    else:
                        print(f"{player1.name} attempts to hit {player2.name} with their {player1.element} bending attacks but misses")
                #user beats
                elif player2.moveChoice[1] == "block" or player2.moveChoice[1] == "attack":
                    attackSuccessfulText = True
                    if player2.moveChoice[1] == "block":
                        print(f"{player1.name} uses their '{player1.moveChoice[0]}' technique to evade {player2.name}'s {player2.element} attacks and successfully hits back")
                    else:
                        print(f"{player1.name} uses their '{player1.moveChoice[0]}' technique to outmaneuver {player2.name}'s {player2.element} attacks and successfully hits back")
                #beats user
                elif player2.moveChoice[1] == "bending" or player2.moveChoice[1] == "observe":
                    if player2.moveChoice[1] == "bending":
                        print(f"{player2.name} is prepared to anticipate and adjust their bending to {player1.name}'s movements")
                    else:
                        print(f"{player1.name}'s movements were anazlysed by {player2.name}")

            #Player Choice being Bending
            elif player1.moveChoice[1] == "bending":
                #same as user
                if player2.moveChoice[1] == "bending":
                    print(f"{player1.name} and {player2.name} both enter a bending showdown")
                    if player1.movePower > player2.movePower:
                        print(f"{player1.name}'s {player1.element} '{player1.moveChoice[0]}' technique is superior to {player2.name}'s bending")
                        attackSuccessfulText = True
                    else:
                        print(f"{player1.name} and {player2.name} bending attacks match up in power with nobody getting ahead")
                #user beats
                elif player2.moveChoice[1] == "block" or player2.moveChoice[1] == "maneuver":
                    attackSuccessfulText = True
                    if player2.moveChoice[1] == "block":
                        print(f"{player1.name}'s {player1.element} '{player1.moveChoice[0]}' technique outperforms {player2.name}'s defensive capabilities")
                    else:
                        print(f"{player1.name} anticipates {player2.name}'s movements and beats them with their {player1.element} '{player1.moveChoice[0]}' bending technique")             
                #beats user
                elif player2.moveChoice[1] == "attack" or player2.moveChoice[1] == "observe":
                    if player2.moveChoice[1] == "attack":
                        print(f"{player2.name}'s {player2.element} bending doesn't match up to {player1.name}'s offensive attacks")
                    else:
                        print(f"{player2.name} analyzes {player1.name}'s {player1.element} bending habits")

            # Activate when the attack is successful
            if attackSuccessfulText:
                damageBeingTaken = 0

                damageBeingTaken += 1

                # Check if player1's move power is greater than player2's defensive stat and the move choices are different
                if player1.movePower >= player2.defensiveStat and player1.moveChoice[1] != player2.moveChoice[1]:
                    print("That was an exceptionally strong move!")
                    strongMoveSuccessful = True
                    # print(f"strong move: {strongMoveSuccessful}")
                    damageBeingTaken += 1

                    # Check if critical hits are active
                    if critsActive:
                        # Test for critical hit with a chance based on critRate
                        # print(f"critical success move: {criticalAttackSuccessful}")
                        if random.randint(1, critRate) == critRate:
                            criticalAttackSuccessful = True
                            damageBeingTaken = criticalAttack(damageBeingTaken, player1)

                # Reduce player2's health by the calculated damage
                if damageBeingTaken == None:
                    if player1.movePower >= player2.defensiveStat and player1.moveChoice[1] != player2.moveChoice[1]:
                        damageBeingTaken = 2
                    else:
                        damageBeingTaken = 1
                    #print("DAMAGE BEING TAKEN ERROR")
                    #input()
                player2.health -= damageBeingTaken
                

                # Print out the zone player2 has been pushed back to (adjust to be modular)
                if player2.health > 0:
                    if player2.health == outsideZone:
                        print(player2.name, "gets pushed back to the outside zone")
                    elif player2.health <= middleZone:
                        print(player2.name, "gets pushed into the middle zone")
                    elif player2.health <= innerZone:
                        print(player2.name, "gets pushed back further into the inner zone")

                # TODO: The following block seems to be commented out, consider removing or adjusting it
                # if False:
                #     if player2.health == innerZone:
                #         print(player2.name, "gets pushed back to the inner zone")
                #     elif player2.health == middleZone:
                #         print(player2.name, "gets pushed back to the middle zone")
                #     elif player2.health == outsideZone:
                #         print(player2.name, "gets pushed back to the outside zone")

                # Increment the count of successful hits for player1
                player1.successfulHits += 1
                # TODO: Uncomment the following line if needed
                # print(player2.name, "gets pushed back to zone", player2.health)




            
            if player2.health <= 0:
                storeBestPlays(player1,player2,strongMoveSuccessful,criticalAttackSuccessful,time)
                if random.randrange(1,10) <= 6:
                    print(player2.name,"gets knocked out of the arena!")
                #elif random.randrange(1,10) <= 4:
                    #print(player2.name,"has been knocked out!")
                else:
                    print(player1.name+"'s last attack managed to knock",player2.name,"out of the arena")
                #player1.knockedoutAmount += 1
    




            if displayStoryText:
                if dialogPlacement == "end" or dialogPlacement == "both":
                    printDialog(player1,player2)
            





# List of attitudes for characters in a conversation
attitude = ["withdrawn", "guarded", "cautious", "neutral", "sociable", "helpful", "forthcoming","positive","neutral","negative"] #basic ["positive","neutral","negative"]

# Topics that can be discussed in various situations
topics = ["personality","actions","connection","goals"]

# Types of actions that can occur in different events or situations
eventActions = ["Attainment","Starting","Neglect","Fight","Recruit","Triumph","Violate","Oppose","Malice","Communicate","Persecute","Increase","Decrease","Abandon","Gratify","Inquire","Antagonise","Move","Waste","Truce","Release","Befriend","Judge","Desert","Dominate","Procrastinate","Praise","Separate","Take","Break","Heal","Delay","Stop","Lie","Return","Immitate","Struggle","Inform","Bestow","Postpone","Expose","Haggle","Imprison","Release","Celebrate","Develop","Travel","Block","Harm","Debase","Overindulge","Adjourn","Adversity","Kill","Disrupt","Usurp","Create","Betray","Agree","Abuse","Oppress","Inspect","Ambush","Spy","Attach","Carry","Open","Carelessness","Ruin","Extravagance","Trick","Arrive","Propose","Divide","Refuse","Mistrust","Deceive","Cruelty","Intolerance","Trust","Excitement","Activity","Assist","Care","Negligence","Passion","Workhard","Control","Attract","Failure","Pursue","Vengeance","Proceedings","Dispute","Punish","Guide","Transform","Overthrow","Oppress","Change"]

# Subjects or themes that events can revolve around
eventSubject = ["Goals","Dreams","Environment","Outside","Inside","Reality","Allies","Enemies","Evil","Good","Emotions","Opposition","War","Peace","The innocent","Love","The spiritual","The intellectual","New ideas","Joy","Messages","Energy","Balance","Tension","Friendship","The physical","A project","Pleasures","Pain","Possessions","Benefits","Plans","Lies","Expectations","Legal matters","Bureaucracy","Business","Apath","News","Exterior factors","Advice","A plot","Competition","Prison","Illness","Food","Attention","Success","Failure","Travel","Jealousy","Dispute","Home","Investment","Suffering","Wishes","Tactics","Stalemate","Randomness","Misfortune","Death","Disruption","Power","Aburden","Intrigues","Fears","Ambush","Rumor","Wounds","Extravagance","A representative","Adversities","Opulence","Liberty","Military","The mundane","Trials","Masses","Vehicle","Art","Victory","Dispute","Riches","Status quo","Technology","Hope","Magic","Illusions","Portals","Danger","Weapons","Animals","Weather","Elements","Nature","The public","Leadership","Fame","Anger","Information"]

# Moods for characters in a conversation
conversationMoods = ["withdrawn", "guarded", "cautious", "neutral", "sociable", "helpful", "forthcoming","positive","neutral","negative"]

# Different bearings characters can have in non-conversation situations
npcBearing = ["intent", "madness", "alliance", "death", "bargain", "fear", "comfort", "capture", "means", "accident", "gratitude", "judgment", "proposition", "chaos", "shelter", "combat", "plan", "idiocy", "happiness", "surrender", "compromise", "illusion", "support", "rage", "agenda", "turmoil", "promise", "resentment", "arrangement", "confusion", "delight", "submission", "negotiation", "façade", "aid", "injury", "plot", "bewilderment", "celebration", "destruction", "questions", "report", "rumor", "reputation", "investigation", "effects", "uncertainty", "doubt", "interest", "examination", "secrets", "bias", "demand", "records", "misdirection", "dislike", "suspicion", "account", "whispers", "partiality", "request", "news", "lies", "belief", "curiosity", "history", "shadows", "view", "skepticism", "telling", "enigma", "discrimination", "command", "discourse", "obscurity", "assessment", "petition", "speech", "conundrum", "difference"]

# Emoticons for use in conversations
emoticons = ["😀", "😃", "😄", "😁", "😆", "😅", "🤣", "😂", "🙂", "😉", "😊", "😇", "🥰", "😍", "🤩", "😘","😗", "☺️", "😚", "😙", "🥲", "😏", "😋", "😛", "😜", "🤪", "😝", "🤗", "🤭", "🫣", "🤫", "🤔", "🫡", "🤤", "🤠", "🥳", "🥸", "😎", "🤓", "🧐", "🙃", "🫠", "🤐", "🤨", "😐", "😑", "😶", "🫥", "😶‍🌫️", "😒", "🙄", "😬", "😮‍💨", "🤥", "😌", "😔", "😪", "😴", "😷", "🤒", "🤕", "🤢", "🤮", "🤧", "🥵", "🥶", "🥴", "😵", "😵‍💫", "🤯", "🥱", "😕", "🫤", "😟", "🙁", "☹️", "😮", "😯", "😲", "😳", "🥺", "🥹", "😦", "😧", "😨", "😰", "😥", "😢", "😭", "😱", "😖", "😣", "😞", "😓", "😩", "😫", "😤", "😡", "😠", "🤬", "👿", "😈", "👿", "💀", "☠️", "💩", "🤡", "😼", "😽", "🙀", "😾", "🙈", "🙉", "🙊", "🐀", "🐓", "🐥", "🐈", "🦊", "🦥", "🪰", "🦄", "🐌", "🦝", "🪳", "🦐", "🐍", "🦎", "🐢"]
emoticonsFaces = ["😀", "😃", "😄", "😁", "😆", "😅", "🤣", "😂", "🙂", "😉", "😊", "😇", "🥰", "😍", "🤩", "😘","😗", "☺️", "😚", "😙", "🥲", "😏", "😋", "😛", "😜", "🤪", "😝", "🤗", "🤭", "🫣", "🤫", "🤔", "🫡", "🤤", "🤠", "🥳", "🥸", "😎", "🤓", "🧐", "🙃", "🫠", "🤐", "🤨", "😐", "😑", "😶", "🫥", "😶‍🌫️", "😒", "🙄", "😬", "😮‍💨", "🤥", "😌", "😔", "😪", "😴", "😷", "🤒", "🤕", "🤢", "🤮", "🤧", "🥵", "🥶", "🥴", "😵", "😵‍💫", "🤯", "🥱", "😕", "🫤", "😟", "🙁", "☹️", "😮", "😯", "😲", "😳", "🥺", "🥹", "😦", "😧", "😨", "😰", "😥", "😢", "😭", "😱", "😖", "😣", "😞", "😓", "😩", "😫", "😤", "😡", "😠", "🤬", "👿", "😈", "👿", "☠️", "🤡", "😼", "😽", "🙀", "😾", "🙈", "🙉", "🙊"]

positiveFaces = ["😀", "😃", "😄", "😁", "😆", "😅", "🤣", "😂", "🙂", "😉", "😊", "😇", "🥰", "😍", "🤩", "😘", "😗", "☺️", "😚", "😙", "🥲", "😌"]
negativeFaces = ["😞", "😓", "😩", "😫", "😤", "😡", "😠", "🤬", "👿", "😈", "👿", "☠️", "🤡", "😼", "😽", "🙀", "😾", "🙈", "🙉", "🙊"]
angryFaces = ["😡", "😠", "🤬", "👿", "😈", "👿", "☠️", "🤡"]
insultFaces = ["😡", "😠", "🤬", "👿", "😈", "👿", "☠️", "🤡", "😼", "😽", "🙀", "😾"]
sadFaces = ["😞", "😓", "😩", "😫", "😤", "😡", "😠", "🤬", "👿", "😈", "👿", "☠️", "😔", "😪", "😢", "😭", "😱", "😖", "😣"]





amountOfRandomPlotTarget = 5
amountOfRandomPlot = 0




listOfTextOptions = ["Character Action", "Monologue", "Conversation", "Scene Description"] #MONOLOGUE = internal dialogue



def emoteConversationGenerator(customRange, cast):
    # Loop for amount of custom range
    for i in range(customRange):
        if random.randint(1,10) <= 7: # If random number then have bigger conversation
            print(f"<{random.choice(cast).name}: {random.choice(emoticons)}>")
            print(f"<{random.choice(cast).name}: {random.choice(emoticons)}>")
        elif random.randint(1,10) <= 5: # Chance to either have internal dialogue or smaller conversation
            print(f"<{random.choice(cast).name}: {random.choice(emoticons)}>")
        else:
            print(f"<<{random.choice(cast).name} monologues {random.choice(emoticons)}>>")
    pass


def generateText(currentCharacter, targetCharacter, situation):
    # If situation is not provided, choose a random one from listOfTextOptions
    if situation is None:
        situation = random.choice(listOfTextOptions)  # Assuming listOfTextOptions is defined somewhere

    # Check the situation and generate text accordingly
    if situation == "Conversation":
        # Check the type of text (text or emoticon) and print accordingly
        if typeOfText == "text":  # Assuming typeOfText is defined somewhere
            print("["+currentCharacter.name+" has a "+random.choice(attitude)+" conversation with "+targetCharacter.name+", Topic: "+random.choice(npcBearing)+" "+random.choice(eventSubject)+"]")
        elif typeOfText == "emoticon":  # Assuming typeOfText is defined somewhere
            print("<"+currentCharacter.name+":", random.choice(emoticons)+">")
            print("<"+targetCharacter.name+":", random.choice(emoticons)+">")

    elif situation == "Monologue":
        if typeOfText == "text":
            print("["+currentCharacter.name+" has a "+random.choice(attitude)+" monologue about "+targetCharacter.name+", Topic: "+random.choice(npcBearing)+" "+random.choice(eventSubject)+"]")
        elif typeOfText == "emoticon":
            print("<<"+random.choice([currentCharacter.name,targetCharacter.name])+" monologues", random.choice(emoticons)+">>")

    elif situation == "Scene Description":
        # randomScenePlots(currentCharacter)  # Assuming this function is defined somewhere
        print("[Scene Description: "+random.choice(eventActions)+" "+random.choice(eventSubject)+"]")
    
    else:
        # Default case for other situations
        print("["+currentCharacter.name+" Character Action Description: "+random.choice(eventActions)+" "+random.choice(eventSubject)+"]")



def generateConversation(currentCharacter,targetCharacter):
    print("conversation")