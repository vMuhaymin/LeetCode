
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
            placement[placementRanked] = ranked[i]
        else:
            placement[placementRanked] = ranked[i]
            placementRanked +=1
    playerStatus= []
    done = False
    i = len(player) - 1
    j= 1
    while(not done):
        playersScore = player[i]
        if j <= len(placement) : 
            score = placement[j]

        if (j > len(placement) and i>= 0):
            playerStatus.append(j)
            if i == 0:
                done = True
        elif playersScore > score and j == 1:
            playerStatus.append(1)
            i-=1
        elif playersScore == score :
            playerStatus.append(j)
            i-=1
        elif  playersScore > score :
            playerStatus.append(j)
            i-=1
        else:
            j+=1
    return reversed(playerStatus)






ranked_count = int(input().strip())

ranked = list(map(int, input().rstrip().split()))

player_count = int(input().strip())

player = list(map(int, input().rstrip().split()))

result = climbingLeaderboard(ranked, player)

print('\n'.join(map(str, result)))

