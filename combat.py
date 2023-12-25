import random
from matchInfo import *

random.seed(int(seed), version=2)

chancesOfDescription = 13#65#/100%
global dialogAmount
dialogAmount = 0
dialogAmountTarget = ((random.randint(45,55))*runs)






displayStoryText = True
        
#zone thresholds
#print(i.name,"the",i.element+"bender - zone",i.health)
innerZone = baseHitTarget
middleZone = round(baseHitTarget/2)
outsideZone = 1





elementBonus = 1.1


critRate = 100
criticalHitText = random.choice(["Flow has been awakened for this attack which causes opponent to get knocked back further!","Which strengthened the attack!"])
critsActive = True








def printCurrentZone(player):
    if player.health == outsideZone:
        print(player.name,"currently in - Inner Zone")
    elif player.health <= middleZone:
        print(player.name,"currently in - Middle Zone")
    elif player.health <= innerZone:
        print(player.name,"currently in - Outside Zone")









def compareStats(player1,player2):
    attackSuccessfulText = False
    print("-")
    if True:
        #print("-")

        printCurrentZone(player1)
    
    if displayStoryText == "run":
        global dialogAmount
        if dialogAmount < dialogAmountTarget:
            if random.randint(1,100) <= chancesOfDescription:
                dialogAmount += 1
                #print(dialogAmount,"/",dialogAmountTarget)
                generateText(player1)
            if random.randint(1,100) <= chancesOfDescription:
                dialogAmount += 1
                #print(dialogAmount,"/",dialogAmountTarget)
                generateText(player2)






    #Element Bonuses
    if player1.element == "Earth" and player2.element == "Water":
        player1.movePower *= elementBonus
    elif player1.element == "Water" and player2.element == "Fire":
        player1.movePower *= elementBonus
    elif player1.element == "Fire" and player2.element == "Air":
        player1.movePower *= elementBonus
    elif player1.element == "Air" and player2.element == "Earth":
        player1.movePower *= elementBonus






#Player Choosing Action for Turn

#Player Choice being Attack
    if player1.moveChoice == "attack":
        #same as user
        if player2.moveChoice == "attack":
            print(player1.name+" and "+player2.name+" enter a offensive showdown")
            if player1.movePower > player2.movePower:
                attackSuccessfulText = True
                print(player1.name+"'s",player1.element+"bending attacks overwhelm "+player2.name)
            else:
                print(player1.name,"tries to hit",player2.name,"with a",player1.element+"bending attack but the shots cancel out")
        #user beats
        elif player2.moveChoice == "observe" or player2.moveChoice == "bending":
            attackSuccessfulText = True
            if player2.moveChoice == "observe":
                print(player1.name+" manages to hit "+player2.name+" with "+player1.element+" attacks while "+player2.name+" is distracted")
            else:
                print(player2.name+"'s bending doesn't match up to "+player1.name+"'s offensive attacks")
        #beats user
        elif player2.moveChoice == "block" or player2.moveChoice == "maneuver":
            if player2.moveChoice == "block":
                print(player2.name+" successfully reflects "+player1.name+"'s "+player1.element+" attacks")
            else:
                print(player2.name+" outmaneuvers "+player1.name+"'s "+player1.element+" attacks")

#Player Choice being Block
    elif player1.moveChoice == "block":
        #same as user
        if player2.moveChoice == "block":
            print(player1.name+" and "+player2.name+" both get into defensive positions")
            if player1.movePower > player2.movePower:
                print(player2.name+"'s",player2.element+"bending shield was too weak for "+player1.name+"'s",player1.element+"bending attacks")
                attackSuccessfulText = True
            else:
                print(player2.name,"manages to block",player1.name+"'s",player1.element+"bending attacks")
        #user beats
        elif player2.moveChoice == "attack" or player2.moveChoice == "observe":
            attackSuccessfulText = True
            if player2.moveChoice == "attack":
                print(player1.name+" successfully counters "+player2.name+"'s "+player2.element+" attacks")
            else:
                print(player1.name+" manages to successfully hit "+player2.name+" as "+player1.name+"'s defensive form was too difficult to analyse")
        #beats user
        elif player2.moveChoice == "maneuver" or player2.moveChoice == "bending":
            if player2.moveChoice == "maneuver":
                print(player2.name+" outmaneuvers "+player1.name+"'s defensive moves")
            else:
                print(player1.name+"'s defensive form doesn't match up to "+player1.name+"'s bending skills")

#Player Choice being Observe
    elif player1.moveChoice == "observe":
        #same as user
        if player2.moveChoice == "observe":
            print(player1.name+" and "+player2.name+" carefully analyse the other's attacks")
            if player1.movePower > player2.movePower:
                print(player1.name,"gets a clean",player1.element+"bending hit against",player2.name)
                attackSuccessfulText = True
            else:
                print(player1.name+"'s",player1.element+" attacks were too easy for",player2.name,"to read")
        #user beats
        elif player2.moveChoice == "bending" or player2.moveChoice == "maneuver":
            attackSuccessfulText = True
            if player2.moveChoice == "bending":
                print(player1.name+" successfully analyses "+player2.name+"'s "+player2.element+"bending habits and sneaks in a hit")
            else:
                print(player1.name+" successfully analyses "+player2.name+"'s movements and predicts their shots to hit "+player2.name)
        #beats user
        elif player2.moveChoice == "attack" or player2.moveChoice == "block":
            if player2.moveChoice == "attack":
                print(player2.name+"'s attacks are too difficult for "+player1.name+" to analyse")
            else:
                print(player2.name+"'s defending moves are too difficult for "+player1.name+" to analyse")

#Player Choice being Maneuver
    elif player1.moveChoice == "maneuver":
        #same as user
        if player2.moveChoice == "maneuver":
            print(player1.name+" and "+player2.name+" are both attempting to secure an advantageous position")
            if player1.movePower > player2.movePower:
                print(player1.name, "skillfully maneuvers and lands a precise", player1.element + " attack against", player2.name)
                attackSuccessfulText = True
            else:
                print(player1.name,"attempts to hit",player2.name,"with their",player1.element+"bending attacks but misses")
        #user beats
        elif player2.moveChoice == "block" or player2.moveChoice == "attack":
            attackSuccessfulText = True
            if player2.moveChoice == "block":
                print(player1.name+" evades "+player2.name+"'s "+player2.element+" attacks and successfully hits back")
            else:
                print(player1.name+" outmaneuvers "+player2.name+"'s "+player2.element+" attacks and successfully hits back")
        #beats user
        elif player2.moveChoice == "bending" or player2.moveChoice == "observe":
            if player2.moveChoice == "bending":
                print(player2.name+"'s bending anticipates and counters "+player1.name+"'s movements")
            else:
                print(player1.name+"'s movements were anazlysed by "+player2.name)

#Player Choice being Bending
    elif player1.moveChoice == "bending":
        #same as user
        if player2.moveChoice == "bending":
            print(player1.name+" and "+player2.name+" both enter a bending showdown")
            if player1.movePower > player2.movePower:
                print(player1.name+"'s",player1.element+"bending is superior to",player2.name+"'s bending")
                attackSuccessfulText = True
            else:
                print(player1.name,"and",player2.name+" bending attacks match up in power with nobody getting ahead")
        #user beats
        elif player2.moveChoice == "block" or player2.moveChoice == "maneuver":
            attackSuccessfulText = True
            if player2.moveChoice == "block":
                print(player1.name+"'s "+player1.element+"bending outperforms "+player2.name+"'s defensive capabilities")
            else:
                print(player1.name+" anticipates "+player2.name+"'s movements and beats them with superior bending")             
        #beats user
        elif player2.moveChoice == "attack" or player2.moveChoice == "observe":
            if player2.moveChoice == "attack":
                print(player2.name+"'s "+player1.element+"bending doesn't match up to "+player1.name+"'s offensive attacks")
            else:
                print(player2.name+" analyzes "+player1.name+"'s "+player1.element+" bending habits")










    #print text for when the attack has been successful and the opponent player gets pushed back
    if attackSuccessfulText:
        damageBeingTaken = 0
        damageBeingTaken += 1
        if player1.movePower > player2.movePower and player1.moveChoice != player2.moveChoice:
            print("That was an exceptionally strong move!")
            damageBeingTaken += 1
        if critsActive: #test out critical hits
            if random.randint(1,critRate) == critRate and player1.moveChoice != player2.moveChoice:
                damageBeingTaken += 1
                print(criticalHitText)

        player2.health -= damageBeingTaken


        #print out what zone player has been pushed back to (adjust to be modular)
        if player2.health > 0:
            if player2.health == outsideZone:
                print(player2.name,"gets pushed back to the outside zone")
            elif player2.health <= middleZone:
                print(player2.name,"gets pushed into the middle zone")
            elif player2.health <= innerZone:
                print(player2.name,"gets pushed back further into the inner zone")
        if False:
            if player2.health == innerZone:
                print(player2.name,"gets pushed back to the inner zone")
            elif player2.health == middleZone:
                print(player2.name,"gets pushed back to the middle zone")
            elif player2.health == outsideZone:
                print(player2.name,"gets pushed back to the outside zone")
        player1.successfulHits+=1
        #print(player2.name,"gets pushed back to zone",player2.health)



    if player2.health <= 0:
        if random.randrange(1,10) <= 6:
            print(player2.name,"gets knocked out of the arena!")
        #elif random.randrange(1,10) <= 4:
            #print(player2.name,"has been knocked out!")
        else:
            print(player1.name+"'s last attack managed to knock",player2.name,"out of the arena")
        #player1.knockedoutAmount += 1





def randomScenePlots(currentCharacter):
    listOfPlotIdeas = [(currentCharacter.name,"awakens their power during the fight"),(currentCharacter.name,"has a pivital character moment")]
    print(random.choice(listOfPlotIdeas))


attitude = ["positive","neutral","negative"]
topics = ["personality","actions","connection","goals"]



#mythicType Generation

eventActions = ["Attainment","Starting","Neglect","Fight","Recruit","Triumph","Violate","Oppose","Malice","Communicate","Persecute","Increase","Decrease","Abandon","Gratify","Inquire","Antagonise","Move","Waste","Truce","Release","Befriend","Judge","Desert","Dominate","Procrastinate","Praise","Separate","Take","Break","Heal","Delay","Stop","Lie","Return","Immitate","Struggle","Inform","Bestow","Postpone","Expose","Haggle","Imprison","Release","Celebrate","Develop","Travel","Block","Harm","Debase","Overindulge","Adjourn","Adversity","Kill","Disrupt","Usurp","Create","Betray","Agree","Abuse","Oppress","Inspect","Ambush","Spy","Attach","Carry","Open","Carelessness","Ruin","Extravagance","Trick","Arrive","Propose","Divide","Refuse","Mistrust","Deceive","Cruelty","Intolerance","Trust","Excitement","Activity","Assist","Care","Negligence","Passion","Workhard","Control","Attract","Failure","Pursue","Vengeance","Proceedings","Dispute","Punish","Guide","Transform","Overthrow","Oppress","Change"]
eventSubject = ["Goals","Dreams","Environment","Outside","Inside","Reality","Allies","Enemies","Evil","Good","Emotions","Opposition","War","Peace","The innocent","Love","The spiritual","The intellectual","New ideas","Joy","Messages","Energy","Balance","Tension","Friendship","The physical","A project","Pleasures","Pain","Possessions","Benefits","Plans","Lies","Expectations","Legal matters","Bureaucracy","Business","Apath","News","Exterior factors","Advice","A plot","Competition","Prison","Illness","Food","Attention","Success","Failure","Travel","Jealousy","Dispute","Home","Investment","Suffering","Wishes","Tactics","Stalemate","Randomness","Misfortune","Death","Disruption","Power","Aburden","Intrigues","Fears","Ambush","Rumor","Wounds","Extravagance","A representative","Adversities","Opulence","Liberty","Military","The mundane","Trials","Masses","Vehicle","Art","Victory","Dispute","Riches","Status quo","Technology","Hope","Magic","Illusions","Portals","Danger","Weapons","Animals","Weather","Elements","Nature","The public","Leadership","Fame","Anger","Information"]









amountOfRandomPlotTarget = 5
amountOfRandomPlot = 0





def generateText(currentCharacter,targetCharacter,specificOne):
    
    if specificOne == None:
        ran = random.randint(1,9)
    else:
        ran = specificOne
    if ran <= 4:
        if random.randint(1,100)<=65:
            print("["+currentCharacter.name+" has a "+random.choice(attitude),"conversation with",targetCharacter.name+", Topic: "+random.choice(eventActions)+" "+random.choice(eventSubject)+"]")
        else:
            print("["+currentCharacter.name+" has a "+random.choice(attitude),"monologue about",targetCharacter.name+", Topic: "+random.choice(eventActions)+" "+random.choice(eventSubject)+"]")
    elif ran <= 7:
        #randomScenePlots(currentCharacter)
        print("[Scene Description: "+random.choice(eventActions)+" "+random.choice(eventSubject)+"]")
    else:
        print("["+currentCharacter.name,"Character Action Description: "+random.choice(eventActions)+" "+random.choice(eventSubject)+"]")
    #print("generating text")


def generateConversation(currentCharacter,targetCharacter):
    print("conversation")