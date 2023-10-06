#custom game engine for Avatar Legends: Onyx Control

#idea; attack, defend, observe & strategize
#stats from 1-100, average % compared to others in program
#team stat too, sum all and divide by 150(?) and thats a stat multiplier before comparesent.
#picks random opponent, each needs to be hit 9 times to be knocked off. (time limit?)
import random, sys, matplotlib.pyplot as plt, numpy as np
from statistics import mean
from scipy.interpolate import make_interp_spline
from combat import *
from matchInfo import *
random.seed(int(seed), version=2)

baseHitTarget = 3
global RedTeam,BlueTeam



xP = []
yPP = []
yP = 0




RedTeam = [Yuka,Asuka,Mei]
BlueTeam = [JinHo,Kaito,Renji]
firstTeamName = "Team Red"
secondTeamName = "Team White"


baseMoveList = ["attack","block","observe"]

global t1W,t2W
t1W=0
t2W=0

winningTeam = None
roundsPassed = 0
totalRoundsPassed = 0
resultsList = []











totalHP1 = 0
totalHP2 = 0
potMVPs = []
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
        yPP.append(yP)
        yP = 0

        for i in team1:
            if i.health<0 or i.health==0:
                print("-----")
                print(i.name,"from",firstTeamName,"has been knocked out!")
                team1.remove(i)
                yP-=1
            else:
                totalHP1 += i.health
        for i in team2:
            if i.health<0 or i.health==0:
                print("-----")
                print(i.name,"from",secondTeamName,"has been knocked out!")
                team2.remove(i)
                yP+=1
            else:
                totalHP2 += i.health





            
        #yP+=(totalHP1-totalHP2) ############################# WORKING HERE ON THIS ALGO

        
        xP.append(totalRoundsPassed)


        




        turnPlayers = team1 + team2
        #turnPlayers.clear()
        #turnPlayers.insert(team1)
        #turnPlayers.insert(team2)
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
                #print out all players for first team
                print(firstTeamName)
                for i in team1:
                    print(i.name,"the",i.element+"bender -",i.health)
                print("-----")
                #print out all players for second team
                print(secondTeamName)
                for i in team2:
                    print(i.name,"the",i.element+"bender -",i.health)
                print("----------")
                turnPlayers.sort(key=lambda x: x.initiative, reverse=True)
                #run combat per player for each team

                for i in turnPlayers:
                    print("-")
                    print(i.name,"-",i.health)
                    compareStats(i,i.target)
                    if i.target.health<0 or i.target.health == 0:
                        if i.target in team1:
                            print(i.target.name,"from",firstTeamName,"has been knocked out!")
                            team1.remove(i.target)
                            turnPlayers.remove(i.target)
                            yP-=1
                        if i.target in team2:
                            print(i.target.name,"from",secondTeamName,"has been knocked out!")
                            team2.remove(i.target)
                            turnPlayers.remove(i.target)
                            yP+=1 






                #for i in team1:
                    #print("-")
                    #print(i.name,"-",i.health)
                    #compareStats(i,i.target)
                #for i in team2:
                    #print("-")
                    #print(i.name,"-",i.health)
                    #compareStats(i,i.target)






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





        #input() #### REMOVE FOR FAST GEN
        
        




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
    potMVPs.append(winners)
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
        print("A draw!",elementChosen+"benders are going to battle this one out!")
        match(teamA,teamB)






yPPAverage = [sum(yPP[:i+1]) / (i+1) for i in range(len(yPP))]


#yPPAverage = []########################### ##### WORKING ON HERE to get average and show a second plot of average throughout the match
#for i in yPP:
#    tempi = sum(yPP[0:i+1]) / len(yPP[0:i+1])

#    yPPAverage.append(tempi)





if displayStoryText == True: ################################### IF DISPLAYSTORYTEXT IS FALSE OR TRUE, CHANGE THIS TOOO
    print("Match Finish!")
else:
    print("Match Finish!")
    print(firstTeamName,":",secondTeamName)
    print((t1W),":",((t2W)))
    print(((t1W/runs)*100),"win %:win %",(((t2W)/runs))*100)
    print("Potential MVPs:",potMVPs)
    print("Round Results:",resultsList)
    print("seed:",seed)

    #PLOTTING PLOT
    plt.figure(figsize=(10, 6))


    #x_smooth = np.linspace(min(xP), max(xP), 100)  # Create a smoother x-axis
    #array1_smooth = make_interp_spline(xP, yPP)(x_smooth)
    #array2_smooth = make_interp_spline(xP, yPPAverage)(x_smooth)





    
    #plt.plot(xP, yPP,marker='o',markersize=3)
    plt.plot(xP, yPPAverage)


    #plt.plot(x_smooth, array1_smooth)
    #plt.plot(x_smooth, array2_smooth)

    # naming the x axis
    plt.xlabel('Rounds')
    # naming the y axis
    plt.ylabel('Advantage')


    plt.annotate(f'{yPPAverage[-1]:.2f}', (xP[-1], yPPAverage[-1]), textcoords="offset points", xytext=(0, 10), ha='center')




    if matchesN == 1:
        plt.xticks(xP)
    # giving a title to my graph
    plt.title('Advantage Plot')
    


    # function to show the plot
    #plt.show()