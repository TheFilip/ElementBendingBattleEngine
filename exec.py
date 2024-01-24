from main import *
#from main import winningTeam







homeTeam = [Yuka,Asuka,Mei]
awayTeam = [JinHo,Kaito,Renji]
#createOwnTeam()



phase1("Team A",homeTeam,"Team B",awayTeam,amountOfRounds=3)

#outputStats(homeTeam)
#outputStats(awayTeam)


while False:
    generateText(random.choice(homeTeam+awayTeam),random.choice(homeTeam+awayTeam),"Scene Description")
    generateText(random.choice(homeTeam+awayTeam),random.choice(homeTeam+awayTeam), None)




    generateText(random.choice(awayTeam),random.choice(homeTeam),None)


    generateText(random.choice(homeTeam),random.choice(awayTeam),None)
    input()