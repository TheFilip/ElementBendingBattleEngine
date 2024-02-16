#characterDB
import random, sys
from matchInfo import *





#[["Swift Strike", "attack"],["Elemental Spike Shield", "block"],["Swift Eyes", "observe"],["Elemental Glide", "maneuver"],["Elemental Surge", "bending"]]
# Canon Avatar Characters
Amon = character_("Amon","Water","Tactician",[["Bending", "bending"]],81,93,63,84,77,61,86,64,79,42,83,86,40,76,58,39)
Unalaq = character_("Unalaq","Water","Zoner",[["Maneuvering", "maneuver"]],57,82,56,66,85,61,75,62,62,40,60,56,37,42,66,37)
Kuruk = character_("Kuruk","Water","Playmaker",[["Observating", "observe"]],55,58,61,65,73,73,94,81,77,85,63,58,83,58,55,93)
Yangchen = character_("Yangchen","Air","Artist",[["Bending", "bending"]],81,74,72,102,77,65,74,77,76,65,57,77,44,55,85,36)
Roku = character_("Roku","Fire","Tactician",[["Bending", "bending"]],58,101,99,60,108,77,86,83,90,74,82,43,38,40,40,37)
Korra = character_("Korra","Water","Brawler",[["Attacking", "attack"]],60,98,86,61,86,74,55,60,39,78,55,82,58,76,63,76)
Kyoshi = character_("Kyoshi","Earth","Brawler",[["Maneuvering", "maneuver"]],64,65,60,66,109,72,56,61,58,82,57,55,80,56,66,99)
Aang = character_("Aang","Air","Artist",[["Attacking", "attack"]],105,93,83,74,72,65,39,77,56,74,82,101,36,87,108,41)
Wan = character_("Wan","Fire","Brawler",[["Attacking", "attack"]],80,64,63,79,76,77,63,65,65,80,85,86,65,62,54,65)
Ozai = character_("Ozai","Fire","Tactician",[["Attacking", "attack"]],65,62,62,62,99,74,80,75,87,61,57,64,61,64,38,79)
Azula = character_("Azula","Fire","Bully",[["Maneuvering", "maneuver"]],86,84,54,74,85,81,78,63,61,44,77,81,42,72,83,55)
JeongJeong = character_("Jeong Jeong","Fire","Artist",[["Bending", "bending"]],64,64,62,66,85,104,54,54,83,86,79,44,59,37,38,40)
Iroh = character_("Iroh","Fire","Tactician",[["Bending", "bending"]],58,64,86,60,86,85,90,94,92,98,81,21,74,42,40,65)
Zuko = character_("Zuko","Fire","Brawler",[["Bending", "bending"]],64,61,56,78,88,74,80,75,74,74,56,77,64,74,55,55)
MonkGyatso = character_("Monk Gyatso","Air","Artist",[["Bending", "bending"]],108,79,65,62,74,61,105,101,94,75,62,58,19,41,61,20)
KingBumi = character_("King Bumi","Earth","Playmaker",[["Attacking", "attack"]],62,83,72,56,84,64,78,65,103,86,74,38,56,36,42,61)
Toph = character_("Toph","Earth","Brawler",[["Bending", "bending"]],61,106,86,80,109,55,43,87,36,83,84,78,64,86,62,56)
Katara = character_("Katara","Water","Playmaker",[["Observating", "observe"]],57,81,85,57,73,84,59,80,88,87,86,64,64,61,64,18)
Tenzin = character_("Tenzin","Air","Lockdown Sweeper",[["Attacking", "attack"]],96,73,65,80,74,57,74,86,84,73,57,84,63,85,82,36)
Kuvira = character_("Kuvira","Earth","Cutman",[["Maneuvering", "maneuver"]],80,73,86,87,110,56,87,87,56,60,84,82,58,86,65,42)
MasterPakku = character_("Master Pakku","Water","Lockdown Sweeper",[["Attacking", "attack"]],59,55,62,56,82,59,59,58,54,62,61,56,40,42,37,20)
Ghazan = character_("Ghazan","Earth","Zoner",[["Observating", "observe"]],86,77,55,84,83,44,41,36,21,20,44,78,21,82,55,58)
Lin = character_("Lin","Earth","Tactician",[["Blocking", "block"]],64,86,58,84,86,61,60,76,54,58,76,74,58,65,36,56)
Suyin = character_("Suyin","Earth","Artist",[["Observating", "observe"]],63,88,59,72,86,62,82,56,58,62,55,56,62,61,38,38)
Bolin = character_("Bolin","Earth","Lockdown Sweeper",[["Attacking", "attack"]],54,110,78,78,76,44,65,55,82,42,85,67,54,83,64,75)
Mako = character_("Mako","Fire","Cutman",[["Bending", "bending"]],62,58,64,62,73,36,57,58,56,59,80,67,64,55,65,64)
Rangi = character_("Rangi","Fire","Lockdown Sweeper",[["Bending", "bending"]],66,73,65,80,78,58,63,61,38,58,77,87,59,59,59,65)
Kya = character_("Kya","Water","Cutman",[["Blocking", "block"]],58,59,62,61,63,42,40,61,55,56,62,62,65,61,62,39)
ChiefTonraq = character_("Chief Tonraq","Water","Brawler",[["Attacking", "attack"]],41,62,59,44,44,42,61,20,39,62,38,65,55,38,37,82)
LongFeng = character_("Long Feng","Earth","Playmaker",[["Maneuvering", "maneuver"]],43,42,38,37,58,36,74,42,62,43,65,19,18,18,22,18)
Desna = character_("Desna","Water","Playmaker",[["Maneuvering", "maneuver"]],66,77,40,61,65,38,20,42,63,44,44,66,43,62,58,41)
Eska = character_("Eska","Water","Zoner",[["Blocking", "block"]],58,75,56,66,56,39,22,39,40,43,38,54,43,59,59,40)
GeneralFong = character_("General Fong","Earth","Wall",[["Attacking", "attack"]],39,56,38,40,40,21,20,39,61,63,58,19,59,43,22,60)
Jinora = character_("Jinora","Air","Artist",[["Maneuvering", "maneuver"]],55,78,59,59,84,86,66,66,93,60,87,82,60,62,61,21)
AdmiralZhao = character_("Admiral Zhao","Fire","Bully",[["Attacking", "attack"]],40,61,41,42,56,64,54,22,20,19,53,20,64,20,21,55)
Meelo = character_("Meelo","Air","Zoner",[["Attacking", "attack"]],63,43,36,58,59,55,43,19,19,21,42,57,18,56,66,21)
Kai = character_("Kai","Air","Cutman",[["Attacking", "attack"]],57,63,38,61,36,40,64,55,63,63,55,63,36,58,56,21)
Opal = character_("Opal","Air","Zoner",[["Attacking", "attack"]],36,41,61,40,40,62,37,78,37,62,65,56,57,39,39,19)
FireNationSoldier = character_("Fire Nation Soldier","Fire","Bully",[["Attacking", "attack"]],21,36,18,38,42,36,39,20,21,22,36,43,21,43,37,20)
Haru = character_("Haru","Earth","Zoner",[["Blocking", "block"]],19,22,66,18,39,18,18,21,44,29,36,36,38,39,18,42)
DaiLi = character_("Dai Li","Earth","Zoner",[["Observating", "observe"]],19,59,44,44,44,40,21,44,18,41,19,19,63,22,20,59)
TheBoulder = character_("The Boulder","Earth","Brawler",[["Observating", "observe"]],19,37,40,21,38,44,20,22,20,19,20,39,20,61,61,22)





bendersMasterList = [Amon, Unalaq, Kuruk, Yangchen, Roku, Korra, Kyoshi, Aang, Wan, Ozai, Azula, JeongJeong, Iroh, 
    Zuko, MonkGyatso, KingBumi, Toph, Katara, Tenzin, Kuvira, MasterPakku, Ghazan, Lin, Suyin, 
    Bolin, Mako, Rangi, Kya, ChiefTonraq, LongFeng, Desna, Eska, GeneralFong, Jinora, AdmiralZhao, 
    Meelo, Kai, Opal, DaiLi, Haru, FireNationSoldier, TheBoulder]

# Separate lists for each element
earthBenders = []
waterBenders = []
airBenders = []
fireBenders = []


# Sort characters into corresponding element lists
for character in bendersMasterList:
    if character.element == 'Earth':
        earthBenders.append(character)
    elif character.element == 'Water':
        waterBenders.append(character)
    elif character.element == 'Air':
        airBenders.append(character)
    elif character.element == 'Fire':
        fireBenders.append(character)

# Sort each element list by name
earthBenders.sort(key=lambda x: x.name, reverse=False)
waterBenders.sort(key=lambda x: x.name, reverse=False)
airBenders.sort(key=lambda x: x.name, reverse=False)
fireBenders.sort(key=lambda x: x.name, reverse=False)

# Combine lists into characterList with separators
characterList = [None]

if earthBenders:
    characterList.extend(earthBenders)
    
if waterBenders:
    characterList.extend(waterBenders)

if airBenders:
    characterList.extend(airBenders)

if fireBenders:
    characterList.extend(fireBenders)
