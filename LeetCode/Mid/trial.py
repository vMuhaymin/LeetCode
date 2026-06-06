def climbingLeaderboard(ranked, player):
    totalPlayers = len(ranked)
    rank = {}
    currenPlayerRank= 1
    for i in range(totalPlayers - 1 , -1 ,-1):         
        if( i - 1 != -2 and ranked[i] == ranked[i - 1]):
            rank[ranked[i]] = currenPlayerRank
            #print('the number is '+str(rank[ranked[i]])+ f' | the actual rank is {ranked[i]}' )
        else: 
            rank[ranked[i]] = currenPlayerRank
            currenPlayerRank +=1
            #print('the number is '+str(rank[ranked[i]])+ f' | the actual rank is {ranked[i]}' )

    totalScore = len(player)
    currPlayerRank= []
    counter = 0
    PlayersCounter = totalScore - 1 # The len of the player's score - 1
    for i in range(totalScore - 1 , -1 , -1):
        done = False
        
        score = player[i]
        while (not done):
            if counter > len(rank) :
                currPlayerRank.append(1)
                #print(f'THE RANK IS THE FIRST ONE ! ')
                done= True
                print("FIRST")
                return currPlayerRank;
            elif (counter == len(rank)  and score == ranked[counter] ):
                currPlayerRank.append(rank[ranked[counter]] +2)
                done= True
                print(f'2nd PLACE WITH RANK { rank[ranked[counter]] +2 } and  score of {score}  Compared with {ranked[counter]} ')
            elif (score > ranked[counter] and counter == 0):
                currPlayerRank.append(rank[ranked[counter]]+1 )
                done= True
                print(f'{rank[ranked[counter]]+1}th PLACE WITH RANK {rank[ranked[counter]]+1} and  score of {score} Compared with {ranked[counter]}')
            elif (score > ranked[counter]):
                currPlayerRank.append(rank[ranked[counter]] )
                done= True
                print(f'The rank of previous of {rank[ranked[counter]]} the score is {score} Compared with {ranked[counter]}')
            elif( score == ranked[counter]):
                done= True
                currPlayerRank.append(rank[ranked[counter]] )
                print(f'Equal Rank! so we appended the {rank[ranked[counter]]} the score is {score} Compared with {ranked[counter]} ')
            counter += 1
        
            
            #For debugging
            # print(f'the rank is {str(rank[ranked[counter]])} and the score is {ranked[counter]}')
            # if counter < 4:
            #     counter += 1
            #     PlayersCounter -= 1
            # else:
            #     done = True
               


Rank = [100,90,90,80,75,60]
list2 = [50,65,77,90,102]

playersRank = climbingLeaderboard(Rank, list2)
for i in playersRank:
    print(f'the player"s rank is {i}')