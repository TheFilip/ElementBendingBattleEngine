#characterDB
import random, sys
from matchInfo import *





#[["Swift Strike", "attack"],["Elemental Spike Shield", "block"],["Swift Eyes", "observe"],["Elemental Glide", "maneuver"],["Elemental Surge", "bending"]]
#EARTH
Yuka = character_("Yuka","Earth","Bully",[["Swift Strike", "attack"]],56,65,36,56,70,49,37,49,26,25,69,44,31,51,56,30)
Asuka = character_("Asuka","Earth","Artist",[["Swift Eyes", "observe"]],71,23,27,36,38,55,52,57,35,35,38,56,29,70,39,25)
Mei = character_("Mei","Earth","Brawler",[["Elemental Glide", "maneuver"]],67,33,63,37,33,55,57,70,60,69,39,70,65,73,50,56)
JinHo = character_("Jin-Ho","Earth","Cutman",[["Swift Strike", "attack"]],72,67,57,70,73,54,54,68,50,60,68,57,61,71,64,63)
Kaito = character_("Kaito","Earth","Tactician",[["Swift Eyes", "observe"]],60,56,33,55,56,48,28,40,29,29,64,36,39,47,48,32)
Renji = character_("Renji","Earth","Brawler",[["Swift Strike", "attack"]],65,45,53,38,35,60,54,43,40,46,50,43,52,57,50,37)
Kim = character_("Kim","Earth","Wall",[["Flair Spike Shield", "block"]],49,48,54,59,50,55,63,49,43,40,47,62,57,48,64,44)
Wenchoi = character_("Wenchoi","Earth","Bully",[["Flair Spike Shield", "block"]],70,51,32,55,56,22,33,40,31,37,60,36,30,38,50,41)
Shoukim = character_("Shoukim","Earth","Lockdown Sweeper",[["Swift Eyes", "observe"]],71,57,64,65,64,60,44,47,57,64,58,63,62,62,67,62)
Chunpang = character_("Chunpang","Earth","Bully",[["Swift Strike", "attack"]],72,44,35,52,43,45,40,42,40,35,48,31,28,43,56,22)
Udeoru = character_("Udeoru","Earth","Wall",[["Swift Eyes", "observe"]],74,78,73,69,61,39,35,38,68,72,66,29,76,45,68,73)
Lamcheung = character_("Lamcheung","Earth","Bully",[["Elemental Surge", "bending"]],49,56,77,46,40,52,59,63,63,65,58,50,67,63,54,72)

Korra = character_("Korra","Water","Bully",[["Super Elemental Surge", "bending"],["Super Elemental Surge", "bending"]],99,99,99,99,99,99,99,99,99,99,99,99,67,63,54,72)


earthBenders = [Yuka, Asuka, Mei, JinHo, Kaito, Renji, Kim,Wenchoi, Shoukim, Chunpang, Udeoru, Lamcheung]
earthBenders.sort(key=lambda x: x.name, reverse=False)
characterList = [None]
characterList.extend(earthBenders)

