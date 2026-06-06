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
        while (not done):
            score = player[PlayersCounter]
            print(f'the rank is {str(rank[ranked[counter]])} and the score is {ranked[counter]}')
            if counter < 4:
                counter += 1
                PlayersCounter -= 1
            else:
                done = True
               
    for i in currPlayerRank:
        print(f'the curr player rank is {currPlayerRank}')

Rank = [100,90, 90, 80 , 60 ]
list2 = [70, 80 , 105]

climbingLeaderboard(Rank, list2)
