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
        self.initiative = (random.randint(1,initiativeMax))+self.initiativeBonus
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


#Korra = character_("Korra","Water",82,55,76,,"attack")
#Mako = character_("Mako","Fire",78,63,67,,"attack")
#Ghazan = character_("Ghazan","Earth",81,43,72,,"observe")
#Kya = character_("Kya","Water",69,83,65,,"observe")
#Azula = character_("Azula","Fire",90,65,69,,"attack")
#Kuvira = character_("Kuvira","Earth",74,58,84,77,"attack")








#EARTH
Yuka = character_("Yuka","Earth",63,30,40,56,"attack")
Asuka = character_("Asuka","Earth",34,29,51,71,"observe")
Mei = character_("Mei","Earth",38,61,64,67,"observe")
JinHo = character_("Jin-Ho","Earth",68,58,58,72,"attack")
Kaito = character_("Kaito","Earth",55,33,36,60,"observe")
Renji = character_("Renji","Earth",43,45,49,65,"attack")
Futai = character_("Futai","Earth",50,72,44,60,"block")
Paiji = character_("Paiji","Earth",56,38,41,72,"attack")
Koteo = character_("Koteo","Earth",60,39,63,75,"observe")
Tsuzen = character_("Tsuzen","Earth",71,57,35,56,"attack")
Bao = character_("Bao","Earth",54,54,36,70,"observe")
Ri = character_("Ri","Earth",48,77,48,51,"attack")
Laoyi = character_("Laoyi","Earth",35,47,44,64,"observe")
Leeshao = character_("Leeshao","Earth",44,44,49,65,"attack")
Tongkawayeung = character_("Tongkawayeung","Earth",52,43,47,66,"attack")
Wonghwang = character_("Wonghwang","Earth",55,52,40,66,"attack")
Upai = character_("Upai","Earth",71,69,34,66,"attack")
Wuliu = character_("Wuliu","Earth",60,69,42,55,"block")
Shoushao = character_("Shoushao","Earth",59,74,70,67,"observe")
Changlichong = character_("Changlichong","Earth",59,42,46,62,"attack")
Ju = character_("Ju","Earth",34,58,57,70,"observe")
Yi = character_("Yi","Earth",69,50,71,59,"attack")
Jisho = character_("Jisho","Earth",25,23,30,54,"block")
Shibak = character_("Shibak","Earth",69,24,46,54,"attack")
Wa = character_("Wa","Earth",45,28,62,46,"attack")
Sueyru = character_("Sueyru","Earth",65,23,46,71,"observe")
Wongchan = character_("Wongchan","Earth",32,68,65,56,"attack")
Khanmi = character_("Khanmi","Earth",48,73,72,68,"observe")
Washaoshi = character_("Washaoshi","Earth",46,66,55,53,"observe")
Choilei = character_("Choilei","Earth",28,70,64,67,"observe")
Mikai = character_("Mikai","Earth",45,31,39,75,"block")
Lichoite = character_("Lichoite","Earth",51,46,58,65,"observe")
Lamno = character_("Lamno","Earth",53,50,70,54,"observe")
Wongmi = character_("Wongmi","Earth",68,54,35,47,"observe")
Thaili = character_("Thaili","Earth",34,62,36,62,"attack")
Changi = character_("Changi","Earth",41,43,41,71,"observe")
Kim = character_("Kim","Earth",53,49,53,49,"block")
Lingmi = character_("Lingmi","Earth",41,62,65,75,"observe")
Jimchen = character_("Jimchen","Earth",31,41,45,50,"attack")
Taichang = character_("Taichang","Earth",53,57,55,65,"block")
Pangka = character_("Pangka","Earth",23,70,70,54,"block")
Kanki = character_("Kanki","Earth",50,54,65,66,"observe")
Leichi = character_("Leichi","Earth",39,64,40,69,"block")
Wenchoi = character_("Wenchoi","Earth",54,33,33,70,"block")
Deono = character_("Deono","Earth",76,40,39,57,"attack")
Dachongyie = character_("Dachongyie","Earth",43,52,52,71,"attack")
Doya = character_("Doya","Earth",72,53,37,64,"observe")
Mayieyie = character_("Mayieyie","Earth",26,50,31,50,"attack")
Shomao = character_("Shomao","Earth",43,58,65,73,"attack")
Wangchunlei = character_("Wangchunlei","Earth",31,62,45,58,"block")
Kowa = character_("Kowa","Earth",31,60,37,67,"block")
Hisho = character_("Hisho","Earth",38,48,58,58,"attack")
Michang = character_("Michang","Earth",53,32,44,49,"observe")
Zhanglao = character_("Zhanglao","Earth",31,58,45,58,"observe")
Wenwen = character_("Wenwen","Earth",78,62,34,65,"block")
Yaochung = character_("Yaochung","Earth",58,60,59,51,"block")
Shoukim = character_("Shoukim","Earth",62,61,55,71,"observe")
Thaizhang = character_("Thaizhang","Earth",25,81,42,49,"block")
Ohwang = character_("Ohwang","Earth",72,71,34,51,"attack")
Wushi = character_("Wu-shi","Earth",60,49,28,43,"attack")
Kungru = character_("Kungru","Earth",44,23,34,55,"observe")
Choi = character_("Choi","Earth",73,43,39,61,"attack")
Nida = character_("Nida","Earth",76,46,68,66,"block")
Uyeung = character_("Uyeung","Earth",47,62,53,54,"observe")
Gepai = character_("Gepai","Earth",27,67,45,62,"block")
Kaya = character_("Kaya","Earth",35,28,27,57,"attack")
Xiuwa = character_("Xiuwa","Earth",66,44,44,68,"block")
Yiega = character_("Yiega","Earth",40,71,63,75,"attack")
Kyoyeung = character_("Kyoyeung","Earth",39,26,65,54,"observe")
Chunpang = character_("Chunpang","Earth",48,31,38,72,"attack")
Udeoru = character_("Udeoru","Earth",68,72,42,74,"attack")
Jilao = character_("Jilao","Earth",65,37,44,47,"attack")
Rasuey = character_("Rasuey","Earth",42,38,33,48,"observe")
Sun = character_("Sun","Earth",73,22,42,58,"block")
Deoyangka = character_("Deoyangka","Earth",61,59,51,58,"attack")
Funo = character_("Funo","Earth",28,42,42,70,"observe")
Kangyie = character_("Kang-yie","Earth",56,67,71,58,"attack")
Choijim = character_("Choijim","Earth",30,37,58,51,"observe")
Fuhi = character_("Fuhi","Earth",54,50,56,56,"block")
Lingdo = character_("Lingdo","Earth",58,35,34,67,"block")
Yamo = character_("Yamo","Earth",44,27,67,61,"observe")
Chikawahon = character_("Chikawahon","Earth",58,46,46,43,"attack")
Rawang = character_("Rawang","Earth",63,25,55,47,"attack")
Laokhan = character_("Laokhan","Earth",70,50,61,72,"attack")
Sado = character_("Sado","Earth",63,66,42,64,"attack")
Parkta = character_("Parkta","Earth",32,55,49,72,"attack")
Ling = character_("Ling","Earth",53,30,60,51,"block")
Daguolong = character_("Daguolong","Earth",69,35,34,48,"block")
Sera = character_("Sera","Earth",42,65,38,57,"attack")
Kawa = character_("Kawa","Earth",35,69,65,63,"observe")
Ruhi = character_("Ruhi","Earth",41,61,57,60,"block")
Uya = character_("Uya","Earth",53,66,32,68,"attack")
Gabao = character_("Gabao","Earth",56,35,52,52,"attack")
Lamcheung = character_("Lamcheung","Earth",50,69,57,49,"block")
Guokawapang = character_("Guokawapang","Earth",67,51,41,57,"observe")
Wenshao = character_("Wenshao","Earth",60,34,57,55,"observe")
Shuwulei = character_("Shuwulei","Earth",46,74,38,75,"observe")
Gachun = character_("Gachun","Earth",56,41,32,50,"attack")
Sako = character_("Sako","Earth",55,63,41,71,"observe")
Caikoge = character_("Caikoge","Earth",36,68,74,55,"block")


#FIRE
Manami = character_("Manami","Fire",57,58,56,72,"attack")
ShirōUma = character_("Shirō Uma","Fire",57,59,59,46,"observe")
TatsujiHijikuro = character_("Tatsuji Hijikuro","Fire",54,67,58,74,"block")
EriNukui = character_("Eri Nukui","Fire",57,59,52,71,"observe")
YūkoKaneyoshi = character_("Yūko Kaneyoshi","Fire",66,57,57,47,"attack")
ShōTonoguchi = character_("Shō Tonoguchi","Fire",51,59,57,66,"attack")
HikariEimori = character_("Hikari Eimori","Fire",60,57,56,59,"observe")
MarinaYoshigoe = character_("Marina Yoshigoe","Fire",55,58,59,47,"block")
YumikaSawataishi = character_("Yumika Sawataishi","Fire",52,48,53,60,"observe")
RyōichiKioi = character_("Ryōichi Kioi","Fire",56,62,61,55,"attack")
SaoriSakaji = character_("Saori Sakaji","Fire",60,59,51,57,"observe")
MunenoriHimejima = character_("Munenori Himejima","Fire",60,57,57,56,"attack")
HirohitoŌgusu = character_("Hirohito Ōgusu","Fire",61,53,59,58,"observe")
ArisaKakusaka = character_("Arisa Kakusaka","Fire",60,59,65,73,"attack")
ChinaTanahashi = character_("China Tanahashi","Fire",55,60,57,74,"observe")
KanamiHirofuji = character_("Kanami Hirofuji","Fire",51,56,60,47,"observe")
MutsumiFujimoto = character_("Mutsumi Fujimoto","Fire",68,58,55,57,"block")
SayakaTakao = character_("Sayaka Takao","Fire",61,61,64,54,"attack")
HisatoShiōchi = character_("Hisato Shiōchi","Fire",61,61,61,65,"attack")
MasanoriKusabuka = character_("Masanori Kusabuka","Fire",61,54,59,69,"block")
TakekoKagawa = character_("Takeko Kagawa","Fire",60,62,68,56,"block")
KatsuhisaEbisuya = character_("Katsuhisa Ebisuya","Fire",58,57,55,72,"block")
MākoŌiwane = character_("Māko Ōiwane","Fire",59,58,61,63,"observe")
KaoriMada = character_("Kaori Mada","Fire",67,73,59,66,"block")
MasatakaNakahodo = character_("Masataka Nakahodo","Fire",54,62,62,70,"block")
HironaoHana = character_("Hironao Hana","Fire",52,55,54,74,"observe")
YūsukeTomita = character_("Yūsuke Tomita","Fire",58,56,54,44,"observe")
SatokaShirahara = character_("Satoka Shirahara","Fire",59,60,55,67,"attack")
HisaKanegawa = character_("Hisa Kanegawa","Fire",53,61,62,75,"block")
MitsushigeNishinoiri = character_("Mitsushige Nishinoiri","Fire",55,53,58,49,"block")
ShihoMoniwa = character_("Shiho Moniwa","Fire",51,63,55,49,"observe")
MamiUnezawa = character_("Mami Unezawa","Fire",59,58,65,63,"attack")
ShinsukeYoshiara = character_("Shinsuke Yoshiara","Fire",62,59,65,70,"observe")
EisakuŌiwane = character_("Eisaku Ōiwane","Fire",60,55,64,43,"attack")
KeiichirōKawazu = character_("Keiichirō Kawazu","Fire",64,54,61,73,"attack")
YūnaSakimoto = character_("Yūna Sakimoto","Fire",61,63,65,50,"block")

#WATER
