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
Futai = character_("Futai","Earth",56,74,34,61,"defend")
Paiji = character_("Paiji","Earth",61,45,42,54,"attack")
Koteo = character_("Koteo","Earth",62,35,72,73,"observe")
Tsuzen = character_("Tsuzen","Earth",73,58,33,29,"attack")
Bao = character_("Bao","Earth",53,55,31,31,"observe")
Ri = character_("Ri","Earth",53,75,38,60,"attack")
Laoyi = character_("Laoyi","Earth",37,44,52,58,"observe")
Leeshao = character_("Leeshao","Earth",46,44,48,56,"attack")
Tongkawayeung = character_("Tongkawayeung","Earth",55,43,43,31,"attack")
Wonghwang = character_("Wonghwang","Earth",53,55,34,43,"attack")
Upai = character_("Upai","Earth",73,71,27,59,"attack")
Wuliu = character_("Wuliu","Earth",56,74,30,47,"defend")
Shoushao = character_("Shoushao","Earth",59,74,69,31,"observe")
Changlichong = character_("Changlichong","Earth",62,48,42,50,"attack")
Ju = character_("Ju","Earth",30,58,54,27,"observe")
Yi = character_("Yi","Earth",71,52,73,27,"attack")
Jisho = character_("Jisho","Earth",29,26,35,40,"defend")
Shibak = character_("Shibak","Earth",71,26,52,33,"attack")
Wa = character_("Wa","Earth",47,29,71,64,"attack")
Sueyru = character_("Sueyru","Earth",68,26,51,41,"observe")
Wongchan = character_("Wongchan","Earth",31,69,64,71,"attack")
Khanmi = character_("Khanmi","Earth",54,75,73,63,"observe")
Washaoshi = character_("Washaoshi","Earth",48,66,50,55,"observe")
Choilei = character_("Choilei","Earth",26,70,60,35,"observe")
Mikai = character_("Mikai","Earth",42,34,40,48,"defend")
Lichoite = character_("Lichoite","Earth",53,42,58,54,"observe")
Lamno = character_("Lamno","Earth",51,50,72,53,"observe")
Wongmi = character_("Wongmi","Earth",66,56,35,37,"observe")
Thaili = character_("Thaili","Earth",34,63,27,51,"attack")
Changi = character_("Changi","Earth",43,36,45,42,"observe")
Kim = character_("Kim","Earth",54,49,54,33,"defend")
Lingmi = character_("Lingmi","Earth",43,63,63,69,"observe")
Jimchen = character_("Jimchen","Earth",29,38,43,36,"attack")
Taichang = character_("Taichang","Earth",55,61,56,55,"defend")
Pangka = character_("Pangka","Earth",25,73,71,26,"defend")
Kanki = character_("Kanki","Earth",54,52,72,68,"observe")
Leichi = character_("Leichi","Earth",35,66,36,41,"defend")
Wenchoi = character_("Wenchoi","Earth",55,32,31,57,"defend")
Deono = character_("Deono","Earth",75,36,40,64,"attack")
Dachongyie = character_("Dachongyie","Earth",38,52,51,66,"attack")
Doya = character_("Doya","Earth",71,48,32,48,"observe")
Mayieyie = character_("Mayieyie","Earth",29,55,26,50,"attack")
Shomao = character_("Shomao","Earth",40,57,66,30,"attack")
Wangchunlei = character_("Wangchunlei","Earth",35,65,45,25,"defend")
Kowa = character_("Kowa","Earth",31,55,33,69,"defend")
Hisho = character_("Hisho","Earth",36,47,59,37,"attack")
Michang = character_("Michang","Earth",50,34,48,63,"observe")
Zhanglao = character_("Zhanglao","Earth",32,61,42,62,"observe")
Wenwen = character_("Wenwen","Earth",75,60,26,61,"defend")
Yaochung = character_("Yaochung","Earth",58,59,61,31,"defend")
Shoukim = character_("Shoukim","Earth",61,59,53,65,"observe")
Thaizhang = character_("Thaizhang","Earth",25,75,33,66,"defend")
Ohwang = character_("Ohwang","Earth",72,63,30,59,"attack")
Wushi = character_("Wushi","Earth",60,49,29,31,"attack")
Kungru = character_("Kungru","Earth",44,25,38,35,"observe")
Choi = character_("Choi","Earth",75,40,37,40,"attack")
Nida = character_("Nida","Earth",74,44,75,27,"defend")
Uyeung = character_("Uyeung","Earth",46,62,48,62,"observe")
Gepai = character_("Gepai","Earth",25,63,43,38,"defend")
Kaya = character_("Kaya","Earth",29,29,30,48,"attack")
Xiuwa = character_("Xiuwa","Earth",67,41,45,46,"defend")
Yiega = character_("Yiega","Earth",37,71,64,39,"attack")
Kyoyeung = character_("Kyoyeung","Earth",39,33,75,53,"observe")
Chunpang = character_("Chunpang","Earth",46,32,38,69,"attack")
Udeoru = character_("Udeoru","Earth",68,71,37,64,"attack")
Jilao = character_("Jilao","Earth",65,40,44,59,"attack")
Rasuey = character_("Rasuey","Earth",38,44,32,40,"observe")
Sun = character_("Sun","Earth",74,27,46,47,"defend")
Deoyangka = character_("Deoyangka","Earth",60,62,55,52,"attack")
Funo = character_("Funo","Earth",29,42,43,59,"observe")
Kangyie = character_("Kangyie","Earth",58,68,74,40,"attack")
Choijim = character_("Choijim","Earth",30,38,68,25,"observe")
Fuhi = character_("Fuhi","Earth",56,43,60,64,"defend")
Lingdo = character_("Lingdo","Earth",57,33,31,38,"defend")
Yamo = character_("Yamo","Earth",46,26,74,38,"observe")
Chikawahon = character_("Chikawahon","Earth",61,49,42,41,"attack")
Rawang = character_("Rawang","Earth",61,29,67,28,"attack")
Laokhan = character_("Laokhan","Earth",67,45,62,61,"attack")
Sado = character_("Sado","Earth",61,70,33,74,"attack")
Parkta = character_("Parkta","Earth",35,55,49,72,"attack")
Ling = character_("Ling","Earth",54,35,68,31,"defend")
Daguolong = character_("Daguolong","Earth",66,38,31,53,"defend")
Sera = character_("Sera","Earth",47,60,35,38,"attack")
Kawa = character_("Kawa","Earth",35,69,65,37,"observe")
Ruhi = character_("Ruhi","Earth",41,58,57,29,"defend")
Uya = character_("Uya","Earth",55,60,26,54,"attack")
Gabao = character_("Gabao","Earth",52,29,60,75,"attack")
Lamcheung = character_("Lamcheung","Earth",49,69,57,72,"defend")
Guokawapang = character_("Guokawapang","Earth",68,56,35,57,"observe")
Wenshao = character_("Wenshao","Earth",65,31,56,62,"observe")
Caikoge = character_("Caikoge","Earth",35,70,73,68,"defend")
Shuwulei = character_("Shuwulei","Earth",56,49,31,65,"attack")
Gachun = character_("Gachun","Earth",55,63,34,41,"observe")
Sako = character_("Sako","Earth",35,70,73,68,"defend")


#FIRE
Manami = character_("Manami","Fire",73,70,33,45,"attack")
ShirōUma = character_("Shirō Uma","Fire",42,30,61,73,"attack")
TatsujiHijikuro = character_("Tatsuji Hijikuro","Fire",50,37,65,59,"observe")
EriNukui = character_("Eri Nukui","Fire",58,39,59,38,"observe")
YūkoKaneyoshi = character_("Yūko Kaneyoshi","Fire",67,25,61,60,"observe")
ShōTonoguchi = character_("Shō Tonoguchi","Fire",55,47,31,53,"observe")
HikariEimori = character_("Hikari Eimori","Fire",46,71,27,67,"attack")


#WATER
Aputi = character_("Aputi","Water",58,46,62,70,"attack")
SunYuNi = character_("Sun Yu-Ni","Water",41,44,35,55,"defend")
ShinSookJa = character_("Shin Sook-Ja","Water",66,51,26,27,"defend")
YiYunJi = character_("Yi Yun-Ji","Water",36,74,54,44,"defend")
PyunWonook = character_("Pyun Won-Sook","Water",62,37,72,29,"observe")
YonTaeRan = character_("Yon Tae-Ran","Water",55,63,42,50,"defend")
PaiJungHyun = character_("Pai Jung-Hyun","Water",62,59,65,73,"observe")