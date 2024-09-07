def cuttingSticks_bottom_up(arr):
    n = len(arr)
    dp = [[0 for i in range(n)] for j in range(n)]
    for l in range(2, n):
        max_i = n - l
        for i in range(n - l):
            j = i + l
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + arr[j] - arr[i])
    return dp[0][n - 1]

if __name__ == "__main__":
    length = int(input())
    cuts = input().split()
    cuts = [int(cut) for cut in cuts]
    cuts = [0] + cuts + [length]
    print(cuttingSticks_bottom_up(cuts))