#Match Info
import random, sys
from collections import Counter


basicFAttackMove  = ["Basic Swift Strike", "attack"]
basicFBlockMove = ["Basic Flair Spike Shield", "block"]
basicFObserveMove = ["Basic Swift Eyes", "observe"]
basicFManeuverMove =["Basic Flair Glide", "maneuver"]
basicFBendingMove = ["Basic Flair Surge", "bending"]

basicAttackMove  = ["Basic Swift Strike", "attack",5]
basicBlockMove = ["Basic Elemental Spike Shield", "block",5]
basicObserveMove = ["Basic Swift Eyes", "observe",5]
basicManeuverMove =["Basic Elemental Glide", "maneuver",5]
basicBendingMove = ["Basic Elemental Surge", "bending",5]
basicPlaymakingMove = ["Basic Playmaking", "playmake",8]

baseMoveList = [basicAttackMove,basicBlockMove,basicObserveMove,basicManeuverMove,basicBendingMove]

#baseMoveList = [["Basic Swift Strike", "attack"],["Basic Elemental Spike Shield", "block"],["Basic Swift Eyes", "observe"],["Basic Elemental Glide", "maneuver"],["Basic Elemental Surge", "bending"]]

global baseHitTarget
baseHitTarget = 3
matchesN = 1
#roundsN = 3


#runs = matchesN*roundsN


modifier = 5 #1 for /100, 5 for /20 stats
variance = 20/modifier #percentage since it adjusts to 100 total


chooseSeed = False
customSeed = 2258881327718708404

if chooseSeed == True:
    seed = customSeed
else:
    seed = random.randrange(sys.maxsize)



#stat bonuses for role
necessaryBonus = 1.2
importantBonus = 1.1
goodBonus = 1.05

elementBonus = 1.1


#function to check player's role and adjust the player's attributes


minimumRollNumber = 1


#supportPositions,defensePositions,offensePositions
#Offense Positions
offensePositions = ["Cutman","Bully","Brawler","Destroyer","Leviathan","Tempest"]
#Defense Positions
defensePositions = ["Zoner","Lockdown Sweeper","Wall","Guardian","Sentinel","Reaper"]
#Support Positions
supportPositions = ["Playmaker","Tactician","Artist","Phantom","Shadow Assassin","Manipulator"]

analyticalPositions = ["Tactician","Zoner","Cutman"]
movementPositions = ["Phantom","Shadow Assassin","Tempest","Reaper"]

allRolesList = offensePositions+defensePositions+supportPositions
elementList = ["Fire","Earth","Water","Air","Nature"]


#= character_("","Water","Bully","observe",62,24,84,86,71,78,80,38,63,54,15,29,63,17,39,68)

#class character2_:
    #def __init__(self,name,element,role,preference,initiative,ElementalPrecision,BendingSpeed,AdaptiveStrategy,TacticalAwareness,Composure,Adaptability,Resilience,PrecisionBlocking,Balance,ElementalDistortion,ElementalReserves,MentalToughness,Agility,Speed,Strength):


# TODO: ADD PERSONALITIES (3 EMOTES THAT GET ADDED AS SELF.PERSONALITY TO EMOTE CONVERSATIONS)
# TODO: ADD STAMINA FOR PLAYERS AND MOVES (MAYBE)
class character_:
    #def __init__(self,name,element,attackStat,blockStat,observeStat,initiativeBonus,preference):
    def __init__(self,name,element,role,preference,initiativeBonus,ElementalPrecision,BendingSpeed,AdaptiveStrategy,TacticalAwareness,Composure,Adaptability,Resilience,PrecisionBlocking,Balance,ElementalDistortion,ElementalReserves,MentalToughness,Agility,Speed,Strength):
        self.name = name
        self.element = element
        self.health = baseHitTarget
        self.healthBackup = baseHitTarget

        # Current Zone Name
        if self.health < round(baseHitTarget/2):
            self.zoneName = "outer zone"
        elif self.health <= round(baseHitTarget/2):
            self.zoneName = "middle zone"
        else:
            self.zoneName = "inner zone"


        if False: # Generate Random Role For Player
            # Use current role as prefered role then randomly choose a role to play as in the match
            self.roleList = supportPositions+defensePositions+offensePositions
            for i in range(9): #odds: 1(+1)/17-11%, 2(+1)/18-16%, 3(+1)/19-21%, 4(+1)/20-25%, 5(+1)/21-29%
                self.roleList.append(role)
            self.role = random.choice(self.roleList)
        else: # Use player's preferred role
            self.role = role



        if self.role in offensePositions:
            self.position = "offense"
        elif self.role in defensePositions:
            self.position = "defense"
        elif self.role in supportPositions:
            self.position = "support"
        else:
            self.position = "other"

        # Levels
        self.level = 1
        self.star = 1

        self.pastMoves = []

        

        


        # Role Bonus Change
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








        



        self.allStats = [initiativeBonus,ElementalPrecision,BendingSpeed,AdaptiveStrategy,TacticalAwareness,Composure,Adaptability,Resilience,PrecisionBlocking,Balance,ElementalDistortion,ElementalReserves,MentalToughness,Agility,Speed,Strength]
        self.allStatsAverage = sum(self.allStats)/len(self.allStats)





        self.attackStat = round(((ElementalPrecision+BendingSpeed+AdaptiveStrategy+Agility+Speed+Strength)/6)/modifier)
        self.blockStat = round(((PrecisionBlocking+Resilience+Composure+Adaptability+ElementalReserves+MentalToughness)/6)/modifier)
        self.observeStat = round(((TacticalAwareness+ElementalPrecision+AdaptiveStrategy+Composure+MentalToughness)/5)/modifier)
        self.maneuverStat = round(((Agility+Speed+Balance+Adaptability+ElementalDistortion)/5)/modifier)
        self.bendingStat = round(((BendingSpeed+ElementalPrecision+ElementalDistortion+ElementalReserves)/4)/modifier)
        self.playmakingStat = round(((AdaptiveStrategy+TacticalAwareness+Composure+Adaptability)/4)/modifier)
        #self.playmakeStat = round((((AdaptiveStrategy + TacticalAwareness + Composure + Adaptability) / 4) * (1 + ((self.level - 1) / 10) + ((self.star - 1) / 100)))/modifier) #<add stars+levels
        self.defensiveStat = round(((Resilience+MentalToughness+Composure+Balance)/4)/modifier)



        
        #print(f"{self.name}: - a{self.attackStat},b {self.blockStat}, o {self.observeStat}, m {self.maneuverStat}, b {self.bendingStat}, p {self.playmakingStat}")



        # Initiative Bonus
        self.initiativeBonus = round(((initiativeBonus+((Speed+Agility)/5)))/modifier)
        self.initiative = 0

        # Amount of times character has successfully knocked out opponent or how many times they have successfully hit
        self.knockedoutAmount = 0
        self.successfulHits = 0



        # Player rating and value
        self.rating = self.allStatsAverage + (self.successfulHits*1.2) + (self.knockedoutAmount*2.4) #Rating is average stats + successful hits and amounts of players knocked out (with a bonus)
        self.value = sum(self.allStats)/len(self.allStats)*(random.randrange(75,125)/100)

        
        #self.movelist = [["Basic Swift Strike", "attack"],["Basic Elemental Spike Shield", "block"],["Basic Swift Eyes", "observe"],["Basic Elemental Glide", "maneuver"],["Basic Elemental Surge", "bending"]]#baseMoveList
        self.movelist =[basicAttackMove,basicBlockMove,basicObserveMove,basicManeuverMove,basicBendingMove]

        # Changes from this list to further down with offense positions and further in blackbox need changing too
        #self.movelist = [["Bending", "bending"],["Maneuvering", "maneuver"],["Attacking", "attack"],["Observating", "observe"],["Blocking", "block"]]
        #self.movelist = [["Basic Swift Strike", "attack"],["Basic Elemental Spike Shield", "block"],["Basic Swift Eyes", "observe"],["Basic Elemental Glide", "maneuver"],["Basic Elemental Surge", "bending"]]#baseMoveList
        #supportPositions,defensePositions,offensePositions
        if self.role in offensePositions:
            self.movelist.append(random.choice([basicAttackMove,basicBendingMove]))
        elif self.role in defensePositions:
            self.movelist.append(random.choice([basicObserveMove,basicBlockMove]))
        elif self.role in supportPositions:
            self.movelist.append(basicPlaymakingMove)

        for i in range(1): #test out doing this twice, odds: 1/6-17%, 2/7-29%, 3/9-33%
            self.movelist.extend(preference)

        self.movePower = 0

    # Reset all player attributes that might change
    def reset(self):
        self.health = baseHitTarget

        # Levels
        self.level = 1
        self.star = 1

        # Initiative Bonus
        self.initiative = 0

        # Amount of times character has successfully knocked out opponent or how many times they have successfully hit
        self.knockedoutAmount = 0
        self.successfulHits = 0

        self.pastMoves = []

    # Choose a random opponent from list of the opposing team
    def chooseRandomOpponent(self, opponentTeam):
        # Create Fresh List
        opponentOptions = []

        # For each enemy in opponent team, take a approximate rating and add to list
        for i in opponentTeam:
            opponentOptions.append([(i.rating*(random.randrange(80,120)/100)),i])
        
        # Sort, lowest to highest perceived rating
        opponentOptions.sort(key=lambda x: x[0])

        if self.role in supportPositions:
            # If the player has a supporting role, chance to attack weakest link in team instead
            if random.randrange(1,2) == 1:
                # Most Dangerous
                mostDangerousOpponent = opponentOptions[-1]
            else:
                # Least Dangerous
                mostDangerousOpponent = opponentOptions[0]

        mostDangerousOpponent = opponentOptions[-1]
        self.target = mostDangerousOpponent[1]#random.choice(opponentTeam)

        #self.initiative = (random.randint(1,variance))+self.initiativeBonus ##



    def checkPastMoves(self,currentMove):
        if len(self.pastMoves) >= 5:
            counts = Counter([sublist[1] for sublist in self.pastMoves])
            if counts[currentMove[1]] >= 2:
                return True
            else:
                #print(f"{self.name}'s past moves: {self.pastMoves} before popping") #####
                self.pastMoves.pop(0)
                #print(f"{self.name}'s past moves: {self.pastMoves} after popping")
                self.pastMoves.append(currentMove[1])
                #print(f"{self.name}'s past moves: {self.pastMoves} new popping") #####
                return False
        else:
            self.pastMoves.append(currentMove[1])
            return False


    def turnChoice(self, ownTeam, opponentTeam):
        self.chooseRandomOpponent(opponentTeam)
        #self.target = random.choice(opponentTeam)
        self.initiative = (random.randint(1,variance))+self.initiativeBonus


        self.moveChoice = self.blackboxDecision(opponentTeam)  # Assuming this is defined elsewhere
        #print(f"{self.name}'s Chosen Move: {self.moveChoice}")print(f"{self.name}'s Chosen Move: {self.moveChoice}")
        while self.checkPastMoves(self.moveChoice):  # Corrected call to checkPastMoves
            print(f"{self.name}'s Chosen Move: {self.moveChoice}")
            self.moveChoice = self.blackboxDecision(opponentTeam)  # Assuming this is defined elsewhere
        #print(f"{self.name}'s Final Chosen Move: {self.moveChoice}")




        if self.moveChoice[1] == "attack":
            self.movePower = random.randrange(minimumRollNumber,self.attackStat)
        elif self.moveChoice[1] == "block":
            self.movePower = random.randrange(minimumRollNumber,self.blockStat)
        elif self.moveChoice[1] == "observe":
            self.movePower = random.randrange(minimumRollNumber,self.observeStat)
        elif self.moveChoice[1] == "maneuver":
            self.movePower = random.randrange(minimumRollNumber,self.maneuverStat)
        elif self.moveChoice[1] == "bending":
            self.movePower = random.randrange(minimumRollNumber,self.bendingStat)
        elif self.moveChoice[1] == "playmake":
            self.movePower = (random.randrange(minimumRollNumber,self.playmakingStat))
        #self.movePower += (random.randint((0-variance),variance))#+moveChoice[2]
            #print(f"a{self.attackStat},b {self.blockStat}, o {self.observeStat}, m {self.maneuverStat}, b {self.bendingStat}, p {self.playmakingStat}")
        #print(f"{self.name}'s movePower: {self.movePower} - {self.moveChoice[1]}")
        

        #Element Bonuses
        if self.element == "Nature" and self.target.element in ["Air","Water"]:
            self.movePower = round(self.movePower*elementBonus)
        elif self.element == "Air" and self.target.element in ["Water","Earth"]:
            self.movePower = round(self.movePower*elementBonus)
        elif self.element == "Water" and self.target.element in ["Earth","Fire"]:
            self.movePower = round(self.movePower*elementBonus)
        elif self.element == "Earth" and self.target.element in ["Fire","Nature"]:
            self.movePower = round(self.movePower*elementBonus)
        elif self.element == "Fire" and self.target.element in ["Nature","Air"]:
            self.movePower = round(self.movePower*elementBonus)


        drunkList.append(self.movePower)
        #print(self.name,self.moveChoice,self.movePower,target.name)
    
    # TODO: MAYBE ADD MEMORY OF LAST OPPONENT MOVE AND USE THAT TO FACTOR IN CURRENT MOVE?



    



        
    def blackboxDecision(self, opponentTeam):
        tempMoveList = self.movelist.copy()
        #tempMoveList = [move.copy() for move in self.movelist]

        # Calculate the average health of all objects in opponent team
        total_opponent_health = sum([opponent.health for opponent in opponentTeam]) if opponentTeam else 0
        opponent_team_health_average = total_opponent_health / len(opponentTeam) if opponentTeam else 0

        #if self.health > opponent_team_health_average:
            #tempMoveList.append(basicAttackMove)
        #elif self.health < opponent_team_health_average:
            #tempMoveList.append(basicBlockMove)
        #else:
            #tempMoveList.append(basicObserveMove)

        if any("playmake" in sublist[1] for sublist in tempMoveList):
            player_stat_weights = {
                "attack": self.attackStat,
                "block": self.blockStat,
                "observe": self.observeStat,
                "maneuver": self.maneuverStat,
                "bending": self.bendingStat,
                "playmake": self.playmakingStat
            }
        else:
            player_stat_weights = {
                "attack": self.attackStat,
                "block": self.blockStat,
                "observe": self.observeStat,
                "maneuver": self.maneuverStat,
                "bending": self.bendingStat,
            }

        # Scale the player stat weights based on random values between og.0.8 and 1.2
        for move_type in player_stat_weights:
            player_stat_weights[move_type] *= random.uniform(0.5, 1.5) # TODO: CHANGE THESE to 0.5/75 - 1.5/25 POTENTIALLY, UNCOMMENT ALL PRINTS AND DEBUG TO FIND BETTER MATHS
        #print(f"{self.name}'s move type stats: {move_type} - {player_stat_weights}")

        # Count occurrences of each move type in tempMoveList
        move_counts = Counter(move[1] for move in tempMoveList)
        #print(f"Move counts: {move_counts}")

        # Calculate appearance weights based on move counts
        move_appearance_weights = {move_type: random.uniform(0.75, 1.25) + move_counts.get(move_type, 0) for move_type in player_stat_weights}
        #print(f"Appearance weights: {move_appearance_weights}")

        # Combine player stat weights and move appearance weights
        combined_weights = {move_type: player_stat_weights[move_type] + move_appearance_weights[move_type]
                            for move_type in player_stat_weights}

        #print(f"{self.name}'s move type combined stats: {move_type} - {combined_weights}")
        # Choose the move type with the highest combined weighted score
        
        chosen_move_type = max(combined_weights, key=combined_weights.get)

        # Filter out moves not present in the movelist
        valid_moves = [move for move in tempMoveList if move[1] == chosen_move_type]

        #print(f"{self.name}'s valid moves: {valid_moves}")

        # Choose a move randomly from the valid_moves list
        choice = random.choice(valid_moves) if valid_moves else random.choice(tempMoveList)
        return choice
        #return random.choice(self.movelist)


#Korra = character_("Korra","Water",82,55,76,,"attack")
#Mako = character_("Mako","Fire",78,63,67,,"attack")
#Ghazan = character_("Ghazan","Earth",81,43,72,,"observe")
#Kya = character_("Kya","Water",69,83,65,,"observe")
#Azula = character_("Azula","Fire",90,65,69,,"attack")
#Kuvira = character_("Kuvira","Earth",74,58,84,77,"attack")






#RedTeam = [Yuka,Asuka,Mei]
#BlueTeam = [JinHo,Kaito,Renji]




