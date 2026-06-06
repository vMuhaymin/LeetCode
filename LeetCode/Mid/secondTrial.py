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
    counter = 1
    for i in range(len(player) - 1, -1 , -1):
        done = False
        score = player[i]
        while (not done):
            if counter > len(placement) :
                playerStatus.append(counter)
                done= True
                print("LAST")
            elif (score > ranked[counter] and counter == 1):
                playerStatus.append(1)
                done= True
                print(f'First with score={ score} > {ranked[counter]}| Rank = {counter}')
            elif (score > ranked[counter] ):
                playerStatus.append(counter-1)
                done= True
                print(f'Bigger than prev with curr score= { score} > {ranked[counter]} | Rank = {counter}')
            elif (counter == len(placement)  and score == ranked[counter] ):
                playerStatus.append(placement[ranked[counter]])
                done= True
                print(f'Equal with curr score= {ranked[counter]} | Rank = {counter}')
            elif (score < ranked[counter] and counter == 0):
                playerStatus.append(placement[ranked[counter]])
                print(f'LAST with curr score= {ranked[counter]} | Rank = {counter}')
                done= True

            elif(counter == 0):
                print(f'{placement[ranked[counter]]}th PLACE WITH RANK {placement[ranked[counter]]} and  score of {score} Compared with {ranked[counter]}')
                return playerStatus;
            elif( score == ranked[counter]):
                done= True
                playerStatus.append(placement[ranked[counter]] )
                print(f'Equal Rank! so we appended the {placement[ranked[counter]]} the score is {score} Compared with {ranked[counter]} ')
            counter += 1

    return playerStatus     


ranked = [100, 90 , 90 , 80]
player = [70,80,105]

playersRank = climbingLeaderboard(ranked, player)
for i in playersRank:
    print(f'the player"s rank is {i}')