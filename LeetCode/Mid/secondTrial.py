def climbingLeaderboard(ranked, player):
    
    placement = {}
    placementRanked = 1
    for i in range(len(ranked)):
        if ( i != len(ranked) - 1 and ranked[i] == ranked[i+1]):
            placement[placementRanked] = ranked[i]
        else:
            placement[placementRanked] = ranked[i]
            placementRanked +=1
    # for i in range(1, len(placement)+1 , 1) :
    #     print(f'the player"s rank is The rank {i} The score -> {placement[i]} ')
    playerStatus= []
    counter = 1
    done = False
    i = len(player) - 1;
    j= 1;

    while(not done):
        playersScore = player[i]
        if j <= len(placement) : 
            score = placement[j]

        if (j > len(placement) and i>= 0):
            playerStatus.append(j)
            print(f'LAST ! with score = {playersScore} and rank= {len(placement) + 1} ' )
            if i == 0:
                done = True

        elif playersScore > score and j == 1:
            playerStatus.append(1)
            print(f'first ! with score= {playersScore}  > {score} and rank= {1} ' )
            i-=1
        elif playersScore == score :
            playerStatus.append(j)
            print(f'Equal ! with score= {playersScore} = {score} and rank= {j} ' )
            i-=1
        elif  playersScore > score :
            playerStatus.append(j)
            print(f'Bigger ! with score= {playersScore} > {score} and rank= {j} ' )
            i-=1
        else:
            j+=1
    return playerStatus

    # while(not done):
    #     print(f'--------------------- ')
    #     print(f'round the i ={i} and j ={j} ')
    #     if(i == 0 and j== len(ranked)-1 ):
    #         playerStatus.append(placement[ranked[j]] )
    #         print(f'The rank of player is {player[i]} = {ranked[j]} with rank of {placement[ranked[j]] } ')
    #         return list(reversed(playerStatus))
    #     elif(i == 0 and j== len(ranked)):
    #         playerStatus.append(placement[ranked[j-1]] + 1)
    #         return list(reversed(playerStatus))
    #     if (i == -1 or j== len(ranked)):
    #         return list(reversed(playerStatus))

    #     if (player[i]>= ranked[j]):
    #         if(player[i]== ranked[j]):
    #             placement[ranked[j]]
    #             playerStatus.append(placement[ranked[j-1]])
    #             print(f'The rank of player is {player[i]} = {ranked[j]} with rank of {placement[ranked[j-1]]} Equal!!!!!!!! ')
    #             i -=1
    #             j +=1
    #         else:
    #             playerStatus.append(placement[ranked[j]])
    #             print(f'The rank of player is {player[i]} > {ranked[j]} with rank of {placement[ranked[j]]}-> Bigger than the prev ')
    #             i -=1
    #             counter +=1
    #     else:
    #         print(f'The score of player is {player[i]} < {ranked[j]}')
    #         j +=1
    #         counter +=1
        
ranked = [100, 90,90,80]
player = [70,80,105]

# ranked = [100, 100,50,40,40,20,10]
# player = [5,25,50,120]

# ranked = [100, 90,90,80,75,60]
# player = [50,65,77,90,102]

# ranked = [100, 90, 80]
# player = [80]

playersRank = climbingLeaderboard(ranked, player)
print('-------------------------------------------')
for i in playersRank:
    print(f'the player"s rank is {i} !!')