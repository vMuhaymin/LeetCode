def climbingLeaderboard(ranked, player):
    totalPlayers = len(ranked)
    rank = {}
    currenPlayerRank= 1
    for i in range(totalPlayers - 1 , -1 ,-1):         
        if( i - 1 != -2 and ranked[i] == ranked[i - 1]):
            rank[i] =  currenPlayerRank
            print(f'the equal ranked is {ranked[i]}' )
        else: 
            rank[i] =  currenPlayerRank
            currenPlayerRank +=1
        print('the number is '+str(rank[i])+ f' | the actual rank is {ranked[i]}' )
    

Rank = [100,90, 90, 80 , 60 ]
list2 = [70, 80 , 105]

climbingLeaderboard(Rank, list2)
