def climbingLeaderboard(ranked, player):
    
    placement = {}
    placementRanked = 1
    print(f'The length is is: {len(ranked)}')

    for i in range(len(ranked)):
        if ( i != len(ranked) - 1 and ranked[i] == ranked[i+1]):
            placement[ranked[i]] = placementRanked
        else:
            placement[ranked[i]] = placementRanked
            placementRanked +=1
    return placement          


ranked = [100,100,50,40,40,20,10]
player = [5, 25,50,120]

playersRank = climbingLeaderboard(ranked, player)
for i in playersRank:
    print(f'the player"s score is {i} with rank of {playersRank[i]}')