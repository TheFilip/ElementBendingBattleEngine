#custom game engine for Avatar Legends: Onyx Control

#idea; attack, defend, observe & strategize
#stats from 1-100, average % compared to others in program
#team stat too, sum all and divide by 150(?) and thats a stat multiplier before comparesent.
#picks random opponent, each needs to be hit 9 times to be knocked off. (time limit?)
import random, sys, matplotlib.pyplot as plt
from combat import *
from MatchInfo import *
random.seed(int(seed), version=2)

baseHitTarget = 3
global RedTeam,BlueTeam



#+x every round
#+y for team 1 knockicking out opponent - -y for team 2 knocking out opponent
xP = []
yPP = []
yP = 0







RedTeam = [Kowa,Yi,Laoyi]
BlueTeam = [Hisho,Uyeung,Wenshao]
firstTeamName = "Team Red"
secondTeamName = "Team White"


baseMoveList = ["attack","defend","observe"]

global t1W,t2W
t1W=0
t2W=0

winningTeam = None
roundsPassed = 0
totalRoundsPassed = 0
resultsList = []











totalHP1 = 0
totalHP2 = 0

turnPlayers = []
def match(team1,team2):
    global teamA, teamB, RedTeam, BlueTeam
    global totalHP1, totalHP2, totalRoundsPassed
    roundsPassed = 0
    roundResults = []

    #t1W=0
    #t2W=0
    while len(team1)>0 and len(team2)>0:
        global yP, xP, yPP
        totalHP1 = 0
        totalHP2 = 0
        for i in team1:
            if i.health<0 or i.health==0:
                print("-----")
                print(i.name,"from",firstTeamName,"has been knocked out!")
                team1.remove(i)
            else:
                totalHP1 += i.health
            #yP-=1
        for i in team2:
            if i.health<0 or i.health==0:
                print("-----")
                print(i.name,"from",secondTeamName,"has been knocked out!")
                team2.remove(i)
            else:
                totalHP2 += i.health
            #yP+=1
        yP=totalHP1-totalHP2 ############################# WORKING HERE ON THIS ALGO

        yPP.append(yP)
        xP.append(totalRoundsPassed)
        turnPlayers.clear()
        turnPlayers.append(team1)
        turnPlayers.append(team2)
        #PRINT HEALTH OF PLAYERS AT START OF ROUND
        print("----------")
        if len(team1) == 0:
            break
        else:
            if len(team2) == 0:
                break
            else:
                roundsPassed += 1
                totalRoundsPassed += 1
        
                print("----- Turn",roundsPassed,"-----")

                for i in team1:
                    i.turnChoice(team2)
                for i in team2:
                    i.turnChoice(team1)
                print(firstTeamName)
                for i in team1:
                    print(i.name,"-",i.health)
                print("-----")
                print(secondTeamName)
                for i in team2:
                    print(i.name,"-",i.health)
                print("----------")
                for i in team1:
                    print("-")
                    print(i.name,"-",i.health)
                    compareStats(i,i.target)
                for i in team2:
                    print("-")
                    print(i.name,"-",i.health)
                    compareStats(i,i.target)
        print("-----")
        for i in team1:
            if i.health<0 or i.health==0:
                print(i.name,"from",firstTeamName,"has been knocked out!")
                team1.remove(i)
                yP-=1
                
        print("-----")
        for i in team2:
            if i.health<0 or i.health==0:
                print(i.name,"from",secondTeamName,"has been knocked out!")
                team2.remove(i)
                yP+=1
        
        
    winners = []
    if len(team1)>len(team2):
        global t1W,t2W
        print(firstTeamName,"Wins!")
        for i in team1:
            winners.append(i.name)
        print(winners)
        print(len(team1),":",len(team2))
        t1W +=1
    elif len(team1)<len(team2):
        print(secondTeamName,"Wins!")
        for i in team2:
            winners.append(i.name)
        print(winners)
        print(len(team1),":",len(team2))
        t2W +=1
    else:
        print("Draw!")
    roundResults = [(len(team1),len(team2))]
    resultsList.append(roundResults)
    print("----- Round Finish -----")



#FIGHT HAPPENS
for i in range(runs):
    for u in RedTeam:
        u.health = baseHitTarget
    for u in BlueTeam:
        u.health = baseHitTarget
    teamA = RedTeam.copy()
    teamB = BlueTeam.copy()
    #teamA = sorted(teamA,key=lambda x:x.defendStat, reverse=False)
    #teamB = sorted(teamB,key=lambda x:x.defendStat, reverse=False)
    match(teamA,teamB)

    if not teamA and not teamB: #IF A DRAW HAPPENS
        for u in RedTeam:
            u.health = baseHitTarget
        for u in BlueTeam:
            u.health = baseHitTarget
        teamA = RedTeam.copy()
        teamB = BlueTeam.copy()
        elementChosen = random.choice(["Earth","Fire","Water"])
        for p in teamA:
            if p.element != elementChosen:
                teamA.remove(p)
        for p in teamB:
            if p.element != elementChosen:
                teamB.remove(p)
        match(teamA,teamB)


if displayStoryText == True: ################################### IF DISPLAYSTORYTEXT IS FALSE OR TRUE, CHANGE THIS TOOO
    print("Match Finish!")
else:
    print("Match Finish!")
    print(firstTeamName,":",secondTeamName)
    print((t1W),":",((t2W)))
    print(((t1W/runs)*100),"win %:win %",(((t2W)/runs))*100)
    print("Round Results: ",resultsList)
    print("seed:",seed)

    #PLOTTING PLOT
    plt.plot(xP, yPP,marker='o',markersize=3)
    # naming the x axis
    plt.xlabel('Rounds')
    # naming the y axis
    plt.ylabel('Advantage')
    
    # giving a title to my graph
    plt.title('Advantage Plot')
    
    # function to show the plot
    plt.show()