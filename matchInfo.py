#Match Info
import random, sys



baseHitTarget = 3
baseMoveList = ["attack","block","observe"]
 

matchesN = 1
roundsN = 3


variance = 20 #percentage since it adjusts to 100 total




chooseSeed = True

if chooseSeed == True:
    seed = 5294566580921762114
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
        self.movelist = baseMoveList
        self.movelist.append(preference)
        self.initiativeBonus = initiativeBonus
        self.initiative = 0

    def turnChoice(self, opponentTeam):
        target = random.choice(opponentTeam)
        self.target = target
        self.initiative = (random.randint(1,variance))+self.initiativeBonus
        while target == self.name:
            target = random.choice(opponentTeam)
        self.moveChoice = random.choice(self.movelist)
        if self.moveChoice == "attack":
            self.movePower = random.randrange(1,self.attackStat)+(random.randint(1,variance))
        if self.moveChoice == "block":
            self.movePower = random.randrange(1,self.blockStat)+(random.randint(1,variance))
        if self.moveChoice == "observe":
            self.movePower = random.randrange(1,self.observeStat)+(random.randint(1,variance))
        #print(self.name,self.moveChoice,self.movePower,target.name)


#Korra = character_("Korra","Water",82,55,76,,"attack")
#Mako = character_("Mako","Fire",78,63,67,,"attack")
#Ghazan = character_("Ghazan","Earth",81,43,72,,"observe")
#Kya = character_("Kya","Water",69,83,65,,"observe")
#Azula = character_("Azula","Fire",90,65,69,,"attack")
#Kuvira = character_("Kuvira","Earth",74,58,84,77,"attack")






#RedTeam = [Yuka,Asuka,Mei]
#BlueTeam = [JinHo,Kaito,Renji]

#EARTH
Yuka = character_("Yuka","Earth",63,30,40,56,"attack")
Asuka = character_("Asuka","Earth",34,29,51,71,"observe")
Mei = character_("Mei","Earth",38,61,64,67,"observe")
JinHo = character_("Jin-Ho","Earth",68,58,58,72,"attack")
Kaito = character_("Kaito","Earth",55,33,36,60,"observe")
Renji = character_("Renji","Earth",43,45,49,65,"attack")



#FIRE


#WATER
