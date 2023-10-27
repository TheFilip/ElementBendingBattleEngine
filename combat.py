import random
from matchInfo import *

random.seed(int(seed), version=2)

chancesOfDescription = 13#65#/100%
global dialogAmount
dialogAmount = 0
dialogAmountTarget = ((random.randint(45,55))*runs)

baseHitTarget = 3





displayStoryText = True
        






elementBonus = 1.1




def compareStats(player1,player2):
    
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



    if player1.element == "Earth" and player2.element == "Water":
        player1.movePower *= elementBonus
    elif player1.element == "Water" and player2.element == "Fire":
        player1.movePower *= elementBonus
    elif player1.element == "Fire" and player2.element == "Earth":
        player1.movePower *= elementBonus

#Player Choice being Attack
    if player1.moveChoice == "attack":
        #same as user
        if player2.moveChoice == "attack":
            if player1.movePower >= player2.movePower:
                player2.health -= 1
                if random.randrange(1,10) <= 7:
                    print(player1.name,"hits",player2.name,"with their",player1.element+"bending")
                else:
                    print(player1.name+"'s",player1.element+"bending shots outperform",player2.name+"'s",player2.element+"bending attacks")
                print(player2.name,"gets pushed back to zone",player2.health)
            else:
                print(player1.name,"tries to hit",player2.name,"with a",player1.element+"bending attack","but the shots cancel out")
        #user beats
        elif player2.moveChoice == "observe":
            if player1.movePower >= player2.movePower:
                player2.health -= 2
                print(player1.name,"lands a strong hit on",player2.name,"with their",player1.element+"bending","while",player2.name,"is distracted")
                print(player2.name,"gets pushed back to zone",player2.health)
            else:
                player2.health -= 1
                print(player1.name,"hits",player2.name,"with their",player1.element+"bending","while",player2.name,"is distracted")
                print(player2.name,"gets pushed back to zone",player2.health)
        #beats user
        elif player2.moveChoice == "block":
            print(player1.name,"tries to hit",player2.name,"with their",player1.element+"bending","but gets blocked")

#Player Choice being Block
    elif player1.moveChoice == "block":
        #same as user
        if player2.moveChoice == "block":
            if player1.movePower >= player2.movePower:
                player2.health -= 1
                print(player1.name,"hits",player2.name,"with their",player1.element+"bending")
                print(player2.name,"gets pushed back to zone",player2.health)
            else:
                print(player2.name,"manages to block",player1.name+"'s",player1.element+"bending attacks")
        #user beats
        elif player2.moveChoice == "attack":
            if player1.movePower >= player2.movePower:
                player2.health -= 2
                print(player1.name,"counters and staggers",player2.name,"with their",player1.element+"bending")
                print(player2.name,"gets pushed back to zone",player2.health)
            else:
                player2.health -= 1
                print(player1.name,"counters",player2.name+"'s",player2.element+"bending attack with their",player1.element+"bending")
                print(player2.name,"gets pushed back to zone",player2.health)
        #beats user
        elif player2.moveChoice == "observe":
            print(player1.name+"'s",player1.element+"bending attack gets read by",player2.name)

#Player Choice being Observe
    elif player1.moveChoice == "observe":
        #same as user
        if player2.moveChoice == "observe":
            if player1.movePower >= player2.movePower:
                player2.health -= 1
                print(player1.name,"gets a clean",player1.element+"bending hit against",player2.name)
                print(player2.name,"gets pushed back to zone",player2.health)
            else:
                print(player1.name,"tries to hit",player2.name,"with their",player1.element+"bending","but misses")
        #user beats
        elif player2.moveChoice == "block":
            if player1.movePower >= player2.movePower:
                player2.health -= 2
                print(player1.name,"pinpoints",player2.name,"with their",player1.element+"bending")
                print(player2.name,"gets pushed back to zone",player2.health)
            else:
                player2.health -= 1
                print(player1.name,"rapid fires",player1.element+"bending attacks and hits",player2.name)
                print(player2.name,"gets pushed back to zone",player2.health)
        #beats user
        elif player2.moveChoice == "attack":
            if random.randrange(1,3) <= 2:
                print(player1.name,"tries to hit",player2.name+", but isn't fast enough")
            else:
                print(player1.name+"'s",player1.element+"bending attacks are too slow for ",player2.name+", all shots miss")
    if player2.health <= 0:
        if random.randrange(1,10) <= 6:
            print(player2.name,"has been knocked out!")
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
            print("["+currentCharacter.name+" has a "+random.choice(attitude),"conversation with",targetCharacter.name+", "+random.choice(eventActions)+" "+random.choice(eventSubject)+"]")
        else:
            print("["+currentCharacter.name+" has a "+random.choice(attitude),"monologue about",targetCharacter.name+", "+random.choice(eventActions)+" "+random.choice(eventSubject)+"]")
    elif ran <= 7:
        #randomScenePlots(currentCharacter)
        print("[Scene Description: "+random.choice(eventActions)+" "+random.choice(eventSubject)+"]")
    else:
        print("["+currentCharacter.name,"Character Action Description: "+random.choice(eventActions)+" "+random.choice(eventSubject)+"]")
    #print("generating text")