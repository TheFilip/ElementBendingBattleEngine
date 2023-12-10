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
    


#Korra = character_("Korra","Water",82,55,76,,"attack")
#Mako = character_("Mako","Fire",78,63,67,,"attack")
#Ghazan = character_("Ghazan","Earth",81,43,72,,"observe")
#Kya = character_("Kya","Water",69,83,65,,"observe")
#Azula = character_("Azula","Fire",90,65,69,,"attack")
#Kuvira = character_("Kuvira","Earth",74,58,84,77,"attack")






#RedTeam = [Yuka,Asuka,Mei]
#BlueTeam = [JinHo,Kaito,Renji]




#EARTH
Yuka = character_("Yuka","Earth",84,27,35,56,"attack")
Asuka = character_("Asuka","Earth",34,27,72,71,"observe")
Mei = character_("Mei","Earth",48,70,55,67,"observe")
JinHo = character_("Jin-Ho","Earth",86,55,68,72,"attack")
Kaito = character_("Kaito","Earth",47,33,40,60,"observe")
Renji = character_("Renji","Earth",58,54,44,65,"attack")
