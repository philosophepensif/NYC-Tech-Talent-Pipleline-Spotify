def changePossibilites(change, coins):
    #temp array, bottom-up dynamic programming - build up solutions temp[m][n-1] is what we are looking for
    # m+1 x n array
    temp = [[0 for i in range(len(coins))] for j in range(change + 1)]
    #base case
    for i in range(0, len(coins)):
        temp[0][i] = 1
    
    for i in range (1, change + 1):
        for j in range(0, len(coins)):
            num_including = 0
            num_excluding = 0
            if i - coins[j] >= 0:
                num_including = temp[i-coins[j]][j]
            if j >=1:
                num_excluding = temp[i][j-1]
            temp[i][j] = num_including + num_excluding
    return temp[change][len(coins) - 1]