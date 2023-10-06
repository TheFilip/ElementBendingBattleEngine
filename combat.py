import random
from matchInfo import *

random.seed(int(seed), version=2)

chancesOfDescription = 65#/100%
global dialogAmount
dialogAmount = 0
dialogAmountTarget = ((random.randint(45,55))*runs)

baseHitTarget = 3
baseMoveList = ["attack","defend","observe"]

displayStoryText = False
        

elementBonus = 1.1




def compareStats(player1,player2):
    
    if displayStoryText == True:
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
                print(player1.name,"hits",player2.name,"with their",player1.element+"bending")
                print(player2.name,"gets pushed back a zone")
            else:
                print(player1.name,"tries to hit",player2.name,"with a",player1.element+"bending attack","but the shots cancel out")
        #user beats
        elif player2.moveChoice == "observe":
            if player1.movePower >= player2.movePower:
                player2.health -= 2
                print(player1.name,"lands a strong hit on",player2.name,"with their",player1.element+"bending","while",player2.name,"is distracted")
                print(player2.name,"gets pushed back 2 zones")
            else:
                player2.health -= 1
                print(player1.name,"hits",player2.name,"with their",player1.element+"bending","while",player2.name,"is distracted")
                print(player2.name,"gets pushed back a zone")
        #beats user
        elif player2.moveChoice == "defend":
            print(player1.name,"tries to hit",player2.name,"with their",player1.element+"bending","but gets blocked")

#Player Choice being Defend
    elif player1.moveChoice == "defend":
        #same as user
        if player2.moveChoice == "defend":
            if player1.movePower >= player2.movePower:
                player2.health -= 1
                print(player1.name,"hits",player2.name,"with their",player1.element+"bending")
                print(player2.name,"gets pushed back a zone")
            else:
                print(player1.name,"tries to hit",player2.name,"with their",player1.element+"bending","but misses")
        #user beats
        elif player2.moveChoice == "attack":
            if player1.movePower >= player2.movePower:
                player2.health -= 2
                print(player1.name,"counters and staggers",player2.name,"with their",player1.element+"bending")
                print(player2.name,"gets pushed back 2 zones")
            else:
                player2.health -= 1
                print(player1.name,"counters",player2.name+"'s",player2.element+"bending attack with their",player1.element+"bending")
                print(player2.name,"gets pushed back a zone")
        #beats user
        elif player2.moveChoice == "observe":
            print(player1.name+"'s",player1.element+"bending attack gets read by",player2.name)

#Player Choice being Observe
    elif player1.moveChoice == "observe":
        #same as user
        if player2.moveChoice == "observe":
            if player1.movePower >= player2.movePower:
                player2.health -= 1
                print(player1.name,"pinpoints",player2.name,"with their",player1.element+"bending")
                print(player2.name,"gets pushed back a zone")
            else:
                print(player1.name,"tries to hit",player2.name,"with their",player1.element+"bending","but misses")
        #user beats
        elif player2.moveChoice == "defend":
            if player1.movePower >= player2.movePower:
                player2.health -= 2
                print(player1.name,"gets a clean",player1.element+"bending hit against",player2.name)
                print(player2.name,"gets pushed back 2 zones")
            else:
                player2.health -= 1
                print(player1.name,"rapid fires",player1.element+"bending attacks and hits",player2.name)
                print(player2.name,"gets pushed back a zone")
        #beats user
        elif player2.moveChoice == "attack":
            print(player1.name,"tries to hit",player2.name+", but isn't fast enough")





attitude = ["Positive","Neutral","Negative"]
def generateText(currentCharacter):
    ran = random.randint(1,9)
    if ran <= 6:
        if random.randint(1,100)<=65:
            print("------",currentCharacter.name,"[Dialog]",random.choice(attitude)," ------")
        else:
            print("------",currentCharacter.name,"[Monologue Dialog]",random.choice(attitude)," ------")
    elif ran <= 8:
        print("------ [Scene Description] ------")
    else:
        print("------",currentCharacter.name,"[Character Action Description] ------")
    #print("generating text")