#custom game engine for Avatar Legends: Onyx Control

#idea; attack, defend, observe & strategize
#stats from 1-100, average % compared to others in program
#team stat too, sum all and divide by 150(?) and thats a stat multiplier before comparesent.
#picks random opponent, each needs to be hit 9 times to be knocked off. (time limit?)
import random, sys
from combat import *
from MatchInfo import *
random.seed(int(seed), version=2)

baseHitTarget = 3
global RedTeam,BlueTeam




RedTeam = [Yuka,Asuka,Mei]
BlueTeam = [JinHo,Kaito,Renji]
firstTeamName = "Team Red"
secondTeamName = "Team Blue"


baseMoveList = ["attack","defend","observe"]

global t1W,t2W
t1W=0
t2W=0

winningTeam = None
roundsPassed = 0
resultsList = []













turnPlayers = []
def match(team1,team2):
    global teamA, teamB, RedTeam, BlueTeam
    roundsPassed = 0
    roundResults = []
    #t1W=0
    #t2W=0
    while len(team1)>0 and len(team2)>0:
        for i in team1:
            if i.health<0 or i.health==0:
                print("-----")
                print(i.name,"from",firstTeamName,"has been knocked out!")
                team1.remove(i)
        for i in team2:
            if i.health<0 or i.health==0:
                print("-----")
                print(i.name,"from",secondTeamName,"has been knocked out!")
                team2.remove(i)
        turnPlayers.clear()
        turnPlayers.append(team1)
        turnPlayers.append(team2)
        print("----------")
        if len(team1) == 0:
            break
        else:
            if len(team2) == 0:
                break
            else:
                roundsPassed += 1
                print("----- Turn",roundsPassed,"-----")
                for i in team1:
                    #print(i.name,"-",i.health)
                    i.turnChoice(team2)
                for i in team2:
                    #print(i.name,"-",i.health)
                    i.turnChoice(team1)
                print("--")
                #print("Team A:")
                for i in team1:
                    print("-")
                    print(i.name,"-",i.health)
                    compareStats(i,i.target)
                    #if i.target.health <= 0:
                        #teamB.remove(i)
                #print("Team B:")
                for i in team2:
                    print("-")
                    print(i.name,"-",i.health)
                    compareStats(i,i.target)
                    #if i.target.health <= 0:
                        #teamA.remove(i)
        for i in team1:
            if i.health<0 or i.health==0:
                print("-----")
                print(i.name,"from",firstTeamName,"has been knocked out!")
                team1.remove(i)
        for i in team2:
            if i.health<0 or i.health==0:
                print("-----")
                print(i.name,"from",secondTeamName,"has been knocked out!")
                team2.remove(i)
        
        
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
