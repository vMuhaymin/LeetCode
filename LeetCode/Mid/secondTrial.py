def climbingLeaderboard(ranked, player):
    
    placement = {}
    placementRanked = 1
    for i in range(len(ranked)):
        if ( i != len(ranked) - 1 and ranked[i] == ranked[i+1]):
            placement[ranked[i]] = placementRanked
        else:
            placement[ranked[i]] = placementRanked
            placementRanked +=1

    
    playerStatus= []
    counter = 0
    for i in range(len(player) - 1, -1 , -1):
        done = False
        score = player[i]
        while (not done):
            if counter > len(placement) :
                playerStatus.append(counter)
                done= True
                print("LAST")
            elif (score > ranked[counter] and counter == 0):
                playerStatus.append(1)
                done= True
                print(f'First with score={ score} > {ranked[counter]}| Rank = {1}')
            elif (score > ranked[counter] ):
                playerStatus.append(counter)
                done= True
                print(f'Bigger than prev with curr score= { score} > {ranked[counter]} | Rank = {counter}')
            elif (score == ranked[counter] ):
                playerStatus.append(placement[ranked[counter]])
                done= True
                print(f'Equal with curr score= {ranked[counter]} | Rank = {counter}')
            elif (score < ranked[counter] and counter == 0):
                playerStatus.append(placement[ranked[counter]+1])
                print(f'LAST with curr score= {ranked[counter]} | Rank = {counter+1}')
                done= True
            counter += 1
    return playerStatus     

# ranked = [100, 90,90,80]
# player = [70,80,105]

# ranked = [100, 90,90,80,75,60]
# player = [50,65,77,90,102]

# ranked = [100, 100,50,40,40,20,10]
# player = [5,25,50,120]






playersRank = climbingLeaderboard(ranked, player)
print('-------------------------------------------')
for i in playersRank:
    print(f'the player"s rank is {i}')