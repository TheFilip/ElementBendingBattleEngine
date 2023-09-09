import random
from MatchInfo import *

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
    if player1.moveChoice == "attack":
        if player2.moveChoice == "attack":
            if player1.movePower >= player2.movePower:
                player2.health -= 1
                print(player1.name,"hits",player2.name)
                print(player2.name,"gets pushed back a zone")
            else:
                print(player1.name,"tries to hit",player2.name,"but all attacks hit each other")
        elif player2.moveChoice == "defend":
            print(player1.name,"tries to hit",player2.name,"but gets blocked")
        elif player2.moveChoice == "observe":
            if player1.movePower >= player2.movePower:
                player2.health -= 2
                print(player1.name,"lands a strong hit on",player2.name,"while they're distracted")
                print(player2.name,"gets pushed back 2 zones")
            else:
                print(player1.name,"hits",player2.name,"while they're distracted")
                player2.health -= 1
                print(player2.name,"gets pushed back a zone")

    elif player1.moveChoice == "defend":
        if player2.moveChoice == "defend":
            if player1.movePower >= player2.movePower:
                player2.health -= 1
                print(player1.name,"hits",player2.name)
                print(player2.name,"gets pushed back a zone")
            else:
                print(player1.name,"tries to hit",player2.name,"but misses")
        elif player2.moveChoice == "observe":
            print(player1.name,"'s attack gets read by",player2.name)
        elif player2.moveChoice == "attack":
            if player1.movePower >= player2.movePower:
                player2.health -= 2
                print(player1.name,"counters and staggers",player2.name)
                print(player2.name,"gets pushed back 2 zones")
            else:
                print(player1.name,"counters",player2.name)
                player2.health -= 1
                print(player2.name,"gets pushed back a zone")

    else:
        if player2.moveChoice == "observe":
            if player1.movePower >= player2.movePower:
                player2.health -= 1
                print(player1.name,"hits",player2.name)
                print(player2.name,"gets pushed back a zone")
            else:
                print(player1.name,"tries to hit",player2.name,"but misses")
        elif player2.moveChoice == "attack":
            print(player1.name,"tries to hit",player2.name,"but isn't fast enough")
        elif player2.moveChoice == "defend":
            if player1.movePower >= player2.movePower:
                player2.health -= 2
                print(player1.name,"gets a clean hit against",player2.name)
                print(player2.name,"gets pushed back 2 zones")
            else:
                print(player1.name,"rapid fires and hits",player2.name)
                player2.health -= 1
                print(player2.name,"gets pushed back a zone")



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