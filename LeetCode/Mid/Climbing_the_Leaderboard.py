
#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

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
    done = False
    i = len(player) - 1;
    j= 0;

    while(not done):
        print(f'--------------------- ')
        print(f'round the i ={i} and j ={j} ')
        if(i == 0 and j== len(ranked)-1 ):
            playerStatus.append(placement[ranked[j]] + 1)
            print(f'The rank of player is {player[i]} = {ranked[j]} with rank of {placement[ranked[j]] + 1} ')
            return list(reversed(playerStatus))
        elif(i == 0 and j== len(ranked)):
            playerStatus.append(placement[ranked[j-1]] + 1)
            return list(reversed(playerStatus))
        if (i == -1 or j== len(ranked)):
            return list(reversed(playerStatus))

        if (player[i]>= ranked[j]):
            if(player[i]== ranked[j]):
                placement[ranked[j]]
                playerStatus.append(placement[ranked[j]])
                print(f'The rank of player is {player[i]} = {ranked[j]} with rank of {placement[ranked[j]]} ')
                i -=1
                j +=1
            else:
                playerStatus.append(placement[ranked[j]])
                print(f'The rank of player is {player[i]} > {ranked[j]} with rank of {placement[ranked[j]]} ')
                i -=1
                counter +=1
        else:
            print(f'The rank of player is {player[i]} < {ranked[j]}')
            j +=1
            counter +=1







ranked_count = int(input().strip())

ranked = list(map(int, input().rstrip().split()))

player_count = int(input().strip())

player = list(map(int, input().rstrip().split()))

result = climbingLeaderboard(ranked, player)

print('\n'.join(map(str, result)))

