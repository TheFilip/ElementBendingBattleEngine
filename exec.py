from main import *
#from main import winningTeam





    
homeTeam = [AputiOkafor, ChewYeongSu, YiYunJi]#[Lamcheung,Kim,Udeoru]#ANGRYGEESE#[Lamcheung,Kim,Udeoru]#[Yuka,Asuka,Mei]
awayTeam = [ChoeJeongHo, ReehSangHoon, MoonSuMin]#[JinHo,Kaito,Renji]#IndustrialHeightsIronclads#[JinHo,Kaito,Renji]#[JinHo,Kaito,Renji]
#createOwnTeam()




#phase1("A",homeTeam,"B",awayTeam)

outputStats(homeTeam,awayTeam)







while False:
    generateText(random.choice(homeTeam+awayTeam),random.choice(homeTeam+awayTeam),7)
    generateText(random.choice(homeTeam+awayTeam),random.choice(homeTeam+awayTeam),None)




    generateText(random.choice(awayTeam),random.choice(homeTeam),None)


    generateText(random.choice(homeTeam),random.choice(awayTeam),None)
    input()