from main import *
#from main import winningTeam








homeTeam = [Wangchunlei,Nida,Sado]#[Yuka,Asuka,Mei]
awayTeam = [Laokhan,Shoushao,Yiega]#[JinHo,Kaito,Renji]







phase1("Home",homeTeam,"Away",awayTeam)

#outputStats(homeTeam,awayTeam)








while False:
    generateText(random.choice(homeTeam+awayTeam),random.choice(homeTeam+awayTeam),7)
    generateText(random.choice(homeTeam+awayTeam),random.choice(homeTeam+awayTeam),None)




    generateText(random.choice(awayTeam),random.choice(homeTeam),None)


    generateText(random.choice(homeTeam),random.choice(awayTeam),None)
    input()