def seqAlign(u, v):
    u = " " + u
    v = " " + v
    dp = [[0 for i in range(len(v))] for j in range(len(u))]
    for i in range(len(u)):
        dp[i][0] = i
    for j in range(len(v)):
        dp[0][j] = j
    for i in range(1, len(u)):
        for j in range(1, len(v)):
            if u[i] == v[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[len(u)-1][len(v)-1]

if __name__ == "__main__":
    u = input()
    v = input()
    print(seqAlign(u, v))