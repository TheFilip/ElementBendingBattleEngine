import random

baseHitTarget = 9
baseMoveList = ["attack","defend","observe"]

class character_:
    def __init__(self,name,element,attackStat,defendStat,observeStat,teamworkStat,preference):
        self.name = name
        self.element = element
        self.health = baseHitTarget
        self.attackStat = attackStat
        self.defendStat = defendStat
        self.observeStat = observeStat
        self.teamworkStat = teamworkStat
        self.movelist = baseMoveList
        self.movelist.append(preference)

    def turnChoice(self, opponentTeam):
        target = random.choice(opponentTeam)
        self.target = target
        while target == self.name:
            target = random.choice(opponentTeam)
        self.moveChoice = random.choice(self.movelist)
        if self.moveChoice == "attack":
            self.movePower = random.randrange(1,self.attackStat)
        if self.moveChoice == "defend":
            self.movePower = random.randrange(1,self.attackStat)
        if self.moveChoice == "observe":
            self.movePower = random.randrange(1,self.observeStat)
        #print(self.name,self.moveChoice,self.movePower,target.name)
        

def compareStats(player1,player2):

    if player1.moveChoice == "attack":
        if player2.moveChoice == "attack":
            if player1.movePower >= player2.movePower:
                player2.health -= 1
                print(player1.name,"hits",player2.name)
                print(player2.name,"gets pushed back a zone")
            else:
                print(player1.name,"tries to hit",player2.name,"but misses")
        elif player2.moveChoice == "defend":
            print(player1.name,"tries to hit",player2.name,"but gets blocked")
        elif player2.moveChoice == "observe":
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
            print(player1.name,"attack gets read by",player2.name)
        elif player2.moveChoice == "attack":
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
            print(player1.name,"tries to hit",player2.name,"but gets nullified")
        elif player2.moveChoice == "defend":
            print(player1.name,"gets a clean hit against",player2.name)
            player2.health -= 1
            print(player2.name,"gets pushed back a zone")