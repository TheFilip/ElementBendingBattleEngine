#Match Info
import random, sys




baseMoveList = ["attack","block","observe"]
 
baseHitTarget = 3
matchesN = 1
roundsN = 3


variance = 20 #percentage since it adjusts to 100 total




chooseSeed = False
customSeed = 6916933039216240636

if chooseSeed == True:
    seed = customSeed
else:
    seed = random.randrange(sys.maxsize)






runs = matchesN*roundsN

class character_:
    def __init__(self,name,element,attackStat,blockStat,observeStat,initiativeBonus,preference):
        self.name = name
        self.element = element
        self.health = baseHitTarget
        self.attackStat = attackStat
        self.blockStat = blockStat
        self.observeStat = observeStat
        self.movelist = ["attack","block","observe"]#baseMoveList
        self.movelist.append(preference)
        self.initiativeBonus = initiativeBonus
        self.initiative = 0

        self.knockedoutAmount = 0

    def chooseRandomOpponent(self, opponentTeam):
        self.target = random.choice(opponentTeam)

    def turnChoice(self, opponentTeam):
        #self.target = random.choice(opponentTeam)
        self.initiative = (random.randint(1,variance))+self.initiativeBonus
        self.moveChoice = random.choice(self.movelist)
        if self.moveChoice == "attack":
            self.movePower = random.randrange(1,self.attackStat)+(random.randint(1,variance))
        if self.moveChoice == "block":
            self.movePower = random.randrange(1,self.blockStat)+(random.randint(1,variance))
        if self.moveChoice == "observe":
            self.movePower = random.randrange(1,self.observeStat)+(random.randint(1,variance))
        #print(self.name,self.moveChoice,self.movePower,target.name)
    


Yuka = character_("Yuka","Earth",63,30,40,56,"attack")
Asuka = character_("Asuka","Earth",34,29,51,71,"observe")
Mei = character_("Mei","Earth",38,61,64,67,"observe")
JinHo = character_("Jin-Ho","Earth",68,58,58,72,"attack")
Kaito = character_("Kaito","Earth",55,33,36,60,"observe")
Renji = character_("Renji","Earth",43,45,49,65,"attack")
