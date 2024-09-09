subset = input("").split() 
subset = [int(i) for i in subset]
target = int(input(""))


def subsetsum(subset, target):
    n = len(subset)
    dp = [[False for i in range(target + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1): #row
        for j in range(1, target + 1): #column
            
            if j < subset[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - subset[i - 1]]
    return dp[n][target]

print(subsetsum(subset, target))