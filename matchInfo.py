#Match Info
import random, sys




baseMoveList = ["attack","block","observe","maneuver","bending"]
 
baseHitTarget = 3
matchesN = 1
roundsN = 1


runs = matchesN*roundsN


variance = 20 #percentage since it adjusts to 100 total




chooseSeed = False
customSeed = 3748094240235785835

if chooseSeed == True:
    seed = customSeed
else:
    seed = random.randrange(sys.maxsize)



#stat bonuses for role
necessaryBonus = 1.2
importantBonus = 1.1
goodBonus = 1.05




#function to check player's role and adjust the player's attributes





#supportPositions,defensePositions,offensePositions
#Offense Positions
offensePositions = ["Cutman","Bully","Brawler","Destroyer","Leviathan","Tempest"]
#Defense Positions
defensePositions = ["Zoner","Lockdown Sweeper","Wall","Guardian","Sentinel","Reaper"]
#Support Positions
supportPositions = ["Playmaker","Tactician","Artist","Phantom","Shadow Assassin","Manipulator"]



#= character_("","Water","Bully","observe",62,24,84,86,71,78,80,38,63,54,15,29,63,17,39,68)

#class character2_:
    #def __init__(self,name,element,role,preference,initiative,ElementalPrecision,BendingSpeed,AdaptiveStrategy,TacticalAwareness,Composure,Adaptability,Resilience,PrecisionBlocking,Balance,ElementalDistortion,ElementalReserves,MentalToughness,Agility,Speed,Strength):



class character_:
    #def __init__(self,name,element,attackStat,blockStat,observeStat,initiativeBonus,preference):
    def __init__(self,name,element,role,preference,initiativeBonus,ElementalPrecision,BendingSpeed,AdaptiveStrategy,TacticalAwareness,Composure,Adaptability,Resilience,PrecisionBlocking,Balance,ElementalDistortion,ElementalReserves,MentalToughness,Agility,Speed,Strength):
        self.name = name
        self.element = element



        self.health = baseHitTarget
        #self.health = baseHitTarget+round(Resilience/16.66666667)



        self.role = role
        #role bonus change
        ####DEFENSIVE
        if role == "Wall":
            #necessary
            Resilience*=necessaryBonus
            #important
            Strength*=importantBonus
            Composure*=importantBonus
            PrecisionBlocking*=importantBonus
            #good
            MentalToughness*=goodBonus
            Speed*=goodBonus
            Balance*=goodBonus
        elif role == "Lockdown Sweeper":
            #necessary
            Composure*=necessaryBonus
            #important
            Strength*=importantBonus
            Resilience*=importantBonus
            ElementalPrecision*=importantBonus
            #good
            Speed*=goodBonus
            BendingSpeed*=goodBonus
            Agility*=goodBonus
        elif role =="Zoner":
            #necessary
            PrecisionBlocking*=necessaryBonus
            #important
            Resilience*=importantBonus
            MentalToughness*=importantBonus
            TacticalAwareness*=importantBonus
            #good
            ElementalReserves*=goodBonus
            AdaptiveStrategy*=goodBonus
            BendingSpeed*=goodBonus
        ####ARTISTS
        elif role == "Artist":
            #necessary
            Agility*=necessaryBonus
            #important
            ElementalReserves*=importantBonus
            Balance*=importantBonus
            AdaptiveStrategy*=importantBonus
            #good
            TacticalAwareness*=goodBonus
            ElementalDistortion*=goodBonus
            Resilience*=goodBonus
        elif role == "Tactician":
            #necessary
            TacticalAwareness*=necessaryBonus
            #important
            AdaptiveStrategy*=importantBonus
            Composure*=importantBonus
            Balance*=importantBonus
            #good
            MentalToughness*=goodBonus
            PrecisionBlocking*=goodBonus
            Adaptability*=goodBonus
        elif role == "Playmaker":
            #necessary
            AdaptiveStrategy*=necessaryBonus
            #important
            TacticalAwareness*=importantBonus
            Agility*=importantBonus
            Adaptability*=importantBonus
            #good
            ElementalPrecision*=goodBonus
            ElementalDistortion*=goodBonus
            Composure*=goodBonus
        ####OFFENSIVE
        elif role == "Bully":
            #necessary
            ElementalPrecision*=necessaryBonus
            #important
            ElementalDistortion*=importantBonus
            BendingSpeed*=importantBonus
            Speed*=importantBonus
            #good
            Adaptability*=goodBonus
            ElementalReserves*=goodBonus
            Strength*=goodBonus
        elif role == "Cutman":
            #necessary
            BendingSpeed*=necessaryBonus
            #important
            Speed*=importantBonus
            Adaptability*=importantBonus
            ElementalReserves*=importantBonus
            #good
            Balance*=goodBonus
            TacticalAwareness*=goodBonus
            PrecisionBlocking*=goodBonus
        elif role == "Brawler":
            #necessary
            Adaptability*=necessaryBonus
            #important
            BendingSpeed*=importantBonus
            ElementalDistortion*=importantBonus
            MentalToughness*=importantBonus
            #good
            Strength*=goodBonus
            Resilience*=goodBonus
            AdaptiveStrategy*=goodBonus

        ##Newest Roles
        elif role == "Leviathan":
            # necessary
            PrecisionBlocking *= necessaryBonus
            # important
            Strength *= importantBonus
            Resilience *= importantBonus
            ElementalDistortion *= importantBonus
            # good
            Speed *= goodBonus
            ElementalReserves *= goodBonus
            MentalToughness *= goodBonus

        elif role == "Tempest":
            # necessary
            ElementalPrecision *= necessaryBonus
            # important
            BendingSpeed *= importantBonus
            Speed *= importantBonus
            Adaptability *= importantBonus
            # good
            MentalToughness *= goodBonus
            TacticalAwareness *= goodBonus
            ElementalReserves *= goodBonus

        elif role == "Phantom":
            # necessary
            Agility *= necessaryBonus
            # important
            Speed *= importantBonus
            ElementalDistortion *= importantBonus
            Balance *= importantBonus
            # good
            MentalToughness *= goodBonus
            TacticalAwareness *= goodBonus
            Adaptability *= goodBonus

        elif role == "Guardian":
            # Necessary
            Resilience *= necessaryBonus
            # Important
            Composure *= importantBonus
            Balance *= importantBonus
            ElementalReserves *= importantBonus
            # Good
            TacticalAwareness *= goodBonus
            MentalToughness *= goodBonus
            Adaptability *= goodBonus

        elif role == "Sentinel":
            # Necessary
            Balance *= necessaryBonus
            # Important
            Resilience *= necessaryBonus
            PrecisionBlocking *= importantBonus
            ElementalPrecision *= importantBonus
            # Good
            TacticalAwareness *= goodBonus
            MentalToughness *= goodBonus
            Speed *= goodBonus

        elif role == "Manipulator":
            # Necessary
            ElementalDistortion *= necessaryBonus
            # Important
            AdaptiveStrategy *= necessaryBonus
            MentalToughness *= importantBonus
            Agility *= importantBonus
            # Good
            ElementalReserves *= goodBonus
            PrecisionBlocking *= goodBonus
            BendingSpeed *= goodBonus

        # AGGRESSIVE
        elif role == "Destroyer":
            # Necessary
            Strength *= necessaryBonus
            # Important
            ElementalPrecision *= necessaryBonus
            Speed *= importantBonus
            ElementalDistortion *= importantBonus
            # Good
            Resilience *= goodBonus
            Adaptability *= goodBonus
            TacticalAwareness *= goodBonus

        elif role == "Shadow Assassin":
            # Necessary
            BendingSpeed *= necessaryBonus
            # Important
            ElementalPrecision *= necessaryBonus
            Speed *= importantBonus
            Agility *= importantBonus
            # Good
            MentalToughness *= goodBonus
            PrecisionBlocking *= goodBonus
            ElementalReserves *= goodBonus

        elif role == "Reaper":
            # necessary
            ElementalDistortion *= necessaryBonus
            # important
            MentalToughness *= importantBonus
            BendingSpeed *= importantBonus
            Agility *= importantBonus
            # good
            TacticalAwareness *= goodBonus
            ElementalPrecision *= goodBonus
            Adaptability *= goodBonus








        #apply stats
        self.level = 1
        self.star = 1



        self.allStats = [initiativeBonus,ElementalPrecision,BendingSpeed,AdaptiveStrategy,TacticalAwareness,Composure,Adaptability,Resilience,PrecisionBlocking,Balance,ElementalDistortion,ElementalReserves,MentalToughness,Agility,Speed,Strength]
        self.allStatsAverage = sum(self.allStats)/len(self.allStats)
        self.value = sum(self.allStats)/len(self.allStats)*(random.randrange(75,125)/100)






        self.attackStat = round((ElementalPrecision+BendingSpeed+AdaptiveStrategy+Agility+Speed+Strength)/6)
        self.blockStat = round((PrecisionBlocking+Resilience+Composure+Adaptability+ElementalReserves+MentalToughness)/6)
        self.observeStat = round((TacticalAwareness+ElementalPrecision+AdaptiveStrategy+Composure+MentalToughness)/5)
        self.maneuverStat = round((Agility+Speed+Balance+Adaptability+ElementalDistortion)/5)
        self.bendingStat = round((BendingSpeed+ElementalPrecision+ElementalDistortion+ElementalReserves)/4)
        #self.playmakeStat = round((AdaptiveStrategy+TacticalAwareness+Composure+Adaptability)/4)
        self.playmakeStat = round(((AdaptiveStrategy + TacticalAwareness + Composure + Adaptability) / 4) * (1 + ((self.level - 1) / 10) + ((self.star - 1) / 100))) #<add stars+levels

        
        self.defensiveStat = round((Resilience+MentalToughness+Composure+Balance)/4)






        self.movelist = ["attack","block","observe","maneuver","bending"]#baseMoveList
        #supportPositions,defensePositions,offensePositions
        if role in offensePositions:
            self.movelist.append(random.choice(["attack","bending"]))
        elif role in defensePositions:
            self.movelist.append(random.choice(["block","observe"]))

        for i in range(1): #test out doing this twice, odds: 1/6-17%, 2/7-29%, 3/9-33%
            self.movelist.extend(preference)



        self.initiativeBonus = round((initiativeBonus+((Speed+Agility)/5)))
        self.initiative = 0

        self.knockedoutAmount = 0
        self.successfulHits = 0

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
        if self.moveChoice == "maneuver":
            self.movePower = random.randrange(1,self.maneuverStat)+(random.randint(1,variance))
        if self.moveChoice == "bending":
            self.movePower = random.randrange(1,self.bendingStat)+(random.randint(1,variance))
        #print(self.name,self.moveChoice,self.movePower,target.name)
    


#Korra = character_("Korra","Water",82,55,76,,"attack")
#Mako = character_("Mako","Fire",78,63,67,,"attack")
#Ghazan = character_("Ghazan","Earth",81,43,72,,"observe")
#Kya = character_("Kya","Water",69,83,65,,"observe")
#Azula = character_("Azula","Fire",90,65,69,,"attack")
#Kuvira = character_("Kuvira","Earth",74,58,84,77,"attack")






#RedTeam = [Yuka,Asuka,Mei]
#BlueTeam = [JinHo,Kaito,Renji]




