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
Futai = character_("Futai","Earth",43,75,52,60,"block")
Paiji = character_("Paiji","Earth",70,39,50,72,"attack")
Koteo = character_("Koteo","Earth",61,42,76,75,"observe")
Tsuzen = character_("Tsuzen","Earth",69,75,39,56,"attack")
Bao = character_("Bao","Earth",48,74,41,70,"observe")
Ri = character_("Ri","Earth",54,71,54,51,"attack")
Laoyi = character_("Laoyi","Earth",35,62,50,64,"observe")
Leeshao = character_("Leeshao","Earth",49,47,63,65,"attack")
Tongkawayeung = character_("Tongkawayeung","Earth",54,58,55,66,"attack")
Wonghwang = character_("Wonghwang","Earth",63,49,34,66,"attack")
Upai = character_("Upai","Earth",73,74,30,66,"attack")
Wuliu = character_("Wuliu","Earth",75,73,48,55,"block")
Shoushao = character_("Shoushao","Earth",63,79,60,67,"observe")
Changlichong = character_("Changlichong","Earth",61,38,51,62,"attack")
Ju = character_("Ju","Earth",31,71,62,70,"observe")
Yi = character_("Yi","Earth",95,52,70,59,"attack")
Jisho = character_("Jisho","Earth",26,20,47,54,"block")
Shibak = character_("Shibak","Earth",70,26,63,54,"attack")
Wa = character_("Wa","Earth",55,35,67,46,"attack")
Sueyru = character_("Sueyru","Earth",63,40,41,71,"observe")
Wongchan = character_("Wongchan","Earth",36,69,70,56,"attack")
Khanmi = character_("Khanmi","Earth",64,69,66,68,"observe")
Washaoshi = character_("Washaoshi","Earth",51,68,71,53,"observe")
Choilei = character_("Choilei","Earth",30,84,72,67,"observe")
Mikai = character_("Mikai","Earth",41,37,44,75,"block")
Lichoite = character_("Lichoite","Earth",65,41,66,65,"observe")
Lamno = character_("Lamno","Earth",69,56,73,54,"observe")
Wongmi = character_("Wongmi","Earth",69,57,37,47,"observe")
Thaili = character_("Thaili","Earth",30,70,37,62,"attack")
Changi = character_("Changi","Earth",46,46,44,71,"observe")
Kim = character_("Kim","Earth",57,67,58,49,"block")
Lingmi = character_("Lingmi","Earth",44,57,75,75,"observe")
Jimchen = character_("Jimchen","Earth",34,41,65,50,"attack")
Taichang = character_("Taichang","Earth",63,48,61,65,"block")
Pangka = character_("Pangka","Earth",32,72,66,54,"block")
Kanki = character_("Kanki","Earth",57,51,71,66,"observe")
Leichi = character_("Leichi","Earth",40,62,51,69,"block")
Wenchoi = character_("Wenchoi","Earth",73,34,36,70,"block")
Deono = character_("Deono","Earth",76,39,46,57,"attack")
Dachongyie = character_("Dachongyie","Earth",56,57,49,71,"attack")
Doya = character_("Doya","Earth",73,58,52,64,"observe")
Mayieyie = character_("Mayieyie","Earth",28,45,49,50,"attack")
Shomao = character_("Shomao","Earth",53,61,74,73,"attack")
Wangchunlei = character_("Wangchunlei","Earth",38,77,51,58,"block")
Kowa = character_("Kowa","Earth",35,68,41,67,"block")
Hisho = character_("Hisho","Earth",58,54,62,58,"attack")
Michang = character_("Michang","Earth",53,42,50,49,"observe")
Zhanglao = character_("Zhanglao","Earth",34,55,48,58,"observe")
Wenwen = character_("Wenwen","Earth",82,58,43,65,"block")
Yaochung = character_("Yaochung","Earth",74,58,56,51,"block")
Shoukim = character_("Shoukim","Earth",60,68,57,71,"observe")
Thaizhang = character_("Thaizhang","Earth",31,86,43,49,"block")
Ohwang = character_("Ohwang","Earth",74,88,35,51,"attack")
Wushi = character_("Wu-shi","Earth",68,47,31,43,"attack")
Kungru = character_("Kungru","Earth",53,24,39,55,"observe")
Choi = character_("Choi","Earth",88,54,41,61,"attack")
Nida = character_("Nida","Earth",76,62,63,66,"block")
Uyeung = character_("Uyeung","Earth",52,70,49,54,"observe")
Gepai = character_("Gepai","Earth",29,85,48,62,"block")
Kaya = character_("Kaya","Earth",29,29,34,57,"attack")
Xiuwa = character_("Xiuwa","Earth",56,47,52,68,"block")
Yiega = character_("Yiega","Earth",43,73,65,75,"attack")
Kyoyeung = character_("Kyoyeung","Earth",50,33,64,54,"observe")
Chunpang = character_("Chunpang","Earth",66,30,40,72,"attack")
Udeoru = character_("Udeoru","Earth",66,81,44,74,"attack")
Jilao = character_("Jilao","Earth",65,32,52,47,"attack")
Rasuey = character_("Rasuey","Earth",41,49,34,48,"observe")
Sun = character_("Sun","Earth",84,21,48,58,"block")
Deoyangka = character_("Deoyangka","Earth",78,61,59,58,"attack")
Funo = character_("Funo","Earth",29,45,51,70,"observe")
Kangyie = character_("Kang-yie","Earth",56,60,72,58,"attack")
Choijim = character_("Choijim","Earth",39,45,51,51,"observe")
Fuhi = character_("Fuhi","Earth",61,58,62,56,"block")
Lingdo = character_("Lingdo","Earth",68,38,36,67,"block")
Yamo = character_("Yamo","Earth",40,23,78,61,"observe")
Chikawahon = character_("Chikawahon","Earth",68,63,52,43,"attack")
Rawang = character_("Rawang","Earth",69,27,65,47,"attack")
Laokhan = character_("Laokhan","Earth",82,52,71,72,"attack")
Sado = character_("Sado","Earth",71,64,50,64,"attack")
Parkta = character_("Parkta","Earth",42,54,56,72,"attack")
Ling = character_("Ling","Earth",61,27,67,51,"block")
Daguolong = character_("Daguolong","Earth",73,34,43,48,"block")
Sera = character_("Sera","Earth",44,58,48,57,"attack")
Kawa = character_("Kawa","Earth",46,69,71,63,"observe")
Ruhi = character_("Ruhi","Earth",39,55,79,60,"block")
Uya = character_("Uya","Earth",65,84,31,68,"attack")
Gabao = character_("Gabao","Earth",63,31,49,52,"attack")
Lamcheung = character_("Lamcheung","Earth",59,65,65,49,"block")
Guokawapang = character_("Guokawapang","Earth",79,44,46,57,"observe")
Wenshao = character_("Wenshao","Earth",63,39,63,55,"observe")
Shuwulei = character_("Shuwulei","Earth",58,83,38,75,"observe")
Gachun = character_("Gachun","Earth",60,59,34,50,"attack")
Sako = character_("Sako","Earth",70,60,47,71,"observe")
Caikoge = character_("Caikoge","Earth",41,80,82,55,"block")


#FIRE


#WATER


#[Atahualpa,Natalija,Adriana]
#[Ragnhild,Chariklia,Frediano]
#og ones
#Atahualpa = character_("Atahualpa","Earth",62,55,61,61,"observe")
#Frediano = character_("Frediano","Earth",57,55,59,60,"attack")
#Natalija = character_("Natalija","Water",55,61,59,72,"attack")
#Chariklia = character_("Chariklia","Water",58,57,57,44,"observe")
#Adriana = character_("Adriana","Fire",62,61,60,69,"observe")
#Ragnhild = character_("Ragnhild","Fire",56,59,58,44,"attack")


Atahualpa = character_("Atahualpa","Earth",57,68,64,65,"attack")
Frediano = character_("Frediano","Earth",49,64,63,73,"block")
Natalija = character_("Natalija","Water",72,60,51,56,"attack")
Chariklia = character_("Chariklia","Water",76,73,59,59,"block")
Adriana = character_("Adriana","Fire",78,57,51,47,"attack")
Ragnhild = character_("Ragnhild","Fire",54,58,81,55,"block")




BerardoParri = character_("Berardo Parri","Fire",39,58,48,67,"block")
KandaWu = character_("Kanda Wu","Fire",117,83,77,93,"observe")
AscanioSinagra = character_("Ascanio Sinagra","Earth",77,92,108,93,"block")
SuJinWu = character_("Su-Jin Wu","Earth",82,103,78,91,"block")
RoccoNannini = character_("Rocco Nannini","Water",63,54,57,88,"attack")
HaiRuan = character_("Hai Ruan","Water",65,29,53,77,"block")