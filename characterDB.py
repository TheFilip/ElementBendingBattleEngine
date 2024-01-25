#characterDB
import random, sys
from matchInfo import *





#[["Swift Strike", "attack"],["elemental Spike Shield", "block"],["Swift Eyes", "observe"],["elemental Glide", "maneuver"],["elemental Surge", "bending"]]
#EARTH
Yuka = character_("Yuka","Earth","Bully",[["Swift Strike", "attack"]],56,65,36,56,70,49,37,49,26,25,69,44,31,51,56,30)
Asuka = character_("Asuka","Earth","Artist",[["Swift Eyes", "observe"]],71,23,27,36,38,55,52,57,35,35,38,56,29,70,39,25)
Mei = character_("Mei","Earth","Brawler",[["Elemental Glide", "maneuver"]],67,33,63,37,33,55,57,70,60,69,39,70,65,73,50,56)
JinHo = character_("Jin-Ho","Earth","Cutman",[["Swift Strike", "attack"]],72,67,57,70,73,54,54,68,50,60,68,57,61,71,64,63)
Kaito = character_("Kaito","Earth","Tactician",[["Swift Eyes", "observe"]],60,56,33,55,56,48,28,40,29,29,64,36,39,47,48,32)
Renji = character_("Renji","Earth","Brawler",[["Swift Strike", "attack"]],65,45,53,38,35,60,54,43,40,46,50,43,52,57,50,37)


earthBenders = [Yuka, Asuka, Mei, JinHo, Kaito, Renji]
earthBenders.sort(key=lambda x: x.name, reverse=False)
characterList = [None]
characterList.extend(earthBenders)

