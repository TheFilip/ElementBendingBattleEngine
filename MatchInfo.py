#Match Info
import random, sys



baseHitTarget = 3
baseMoveList = ["attack","defend","observe"]
 
matchesN = 1
roundsN = 3
runs = matchesN*roundsN


chooseSeed = True

if chooseSeed == True:
    seed = 9102585960368991521
else:
    seed = random.randrange(sys.maxsize)








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





#EARTH
Yuka = character_("Yuka","Earth",60,33,47,51,"attack")
Asuka = character_("Asuka","Earth",29,33,62,44,"observe")
Mei = character_("Mei","Earth",43,66,64,51,"observe")
JinHo = character_("JinHo","Earth",64,60,61,44,"attack")
Kaito = character_("Kaito","Earth",56,29,38,37,"observe")
Renji = character_("Renji","Earth",44,47,53,25,"attack")