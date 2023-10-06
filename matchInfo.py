#Match Info
import random, sys



baseHitTarget = 3
baseMoveList = ["attack","block","observe"]
 

matchesN = 1
roundsN = 3


initiativeMax = 20




chooseSeed = True

if chooseSeed == True:
    seed = 9102585960368991521
else:
    seed = random.randrange(sys.maxsize)






runs = matchesN*roundsN

class character_:
    def __init__(self,name,element,attackStat,blockStat,observeStat,preference):
        self.name = name
        self.element = element
        self.health = baseHitTarget
        self.attackStat = attackStat
        self.blockStat = blockStat
        self.observeStat = observeStat
        self.movelist = baseMoveList
        self.movelist.append(preference)
        self.initiative = 0

    def turnChoice(self, opponentTeam):
        target = random.choice(opponentTeam)
        self.target = target
        self.initiative = random.randint(1,initiativeMax)
        while target == self.name:
            target = random.choice(opponentTeam)
        self.moveChoice = random.choice(self.movelist)
        if self.moveChoice == "attack":
            self.movePower = random.randrange(1,self.attackStat)
        if self.moveChoice == "block":
            self.movePower = random.randrange(1,self.blockStat)
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
Yuka = character_("Yuka","Fire",57,48,52,"block")
Asuka = character_("Asuka","Earth",72,41,81,"observe")
Mei = character_("Mei","Water",53,49,47,"attack")
JinHo = character_("Jin-Ho","Earth",45,68,61,"attack")
Kaito = character_("Kaito","Fire",37,43,51,"attack")
Renji = character_("Renji","Earth",53,57,78,"block")



#FIRE


#WATER
