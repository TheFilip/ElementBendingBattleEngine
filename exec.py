from main import *
#from main import winningTeam



#when recording, record in parts (like a mumbojumbo episode (or a ethoslab?)). talk about stuff in parts
##and when making video, some cools parts per round put up anime clips of what it would be looking like when this happens
###talk about what is happening?? like a amagi video?



#make it so if True, then no text will be displayed just who won the match and the MVPs



winningName = "xx"
#winningTeam="2"
#homeTeam = [Yuka,Asuka,Mei]
#awayTeam = [JinHo,Kaito,Renji]
homeTeam=[JinHo,Kaito,Renji]#[Caikoge,Leichi,Ohwang]
awayTeam=[Wenchoi,Chunpang,Shoukim]#[Sun,Pangka,Sueyru]





#program("Home",homeTeam,"Away",awayTeam)



while False:
    generateText(random.choice(homeTeam+awayTeam),random.choice(homeTeam+awayTeam),7)
    generateText(random.choice(homeTeam+awayTeam),random.choice(homeTeam+awayTeam),None)




    generateText(random.choice(awayTeam),random.choice(homeTeam),None)


    generateText(random.choice(homeTeam),random.choice(awayTeam),None)
    input()