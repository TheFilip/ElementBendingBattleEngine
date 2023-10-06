#Match Info
import random, sys



baseHitTarget = 3
baseMoveList = ["attack","defend","observe"]
 

matchesN = 1
roundsN = 3







chooseSeed = False

if chooseSeed == True:
    seed = 9102585960368991521
else:
    seed = random.randrange(sys.maxsize)






runs = matchesN*roundsN

class character_:
    def __init__(self,name,element,attackStat,defendStat,observeStat,preference):
        self.name = name
        self.element = element
        self.health = baseHitTarget
        self.attackStat = attackStat
        self.defendStat = defendStat
        self.observeStat = observeStat
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
            self.movePower = random.randrange(1,self.defendStat)
        if self.moveChoice == "observe":
            self.movePower = random.randrange(1,self.observeStat)
        #print(self.name,self.moveChoice,self.movePower,target.name)


Korra = character_("Korra","Water",82,55,76,"attack")
Mako = character_("Mako","Fire",78,63,67,"attack")
Ghazan = character_("Ghazan","Earth",81,43,72,"observe")
Kya = character_("Kya","Water",69,83,65,"observe")
Azula = character_("Azula","Fire",90,65,69,"attack")
Kuvira = character_("Kuvira","Earth",74,58,84,"attack")








#EARTH
Yuka = character_("Yuka","Earth",63,30,40,"attack")
Asuka = character_("Asuka","Earth",34,29,51,"observe")
Mei = character_("Mei","Earth",38,61,64,"observe")
JinHo = character_("Jin-Ho","Earth",68,58,58,"attack")
Kaito = character_("Kaito","Earth",55,33,36,"observe")
Renji = character_("Renji","Earth",43,45,49,"attack")

#FIRE

#WATER
