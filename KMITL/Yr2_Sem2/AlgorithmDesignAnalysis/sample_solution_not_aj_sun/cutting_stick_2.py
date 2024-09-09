length = input("")
length = int(length)

cut = input("")
cut = cut.split(" ")

cut = [int(i) for i in cut]

def cutting_stick(length, cut):
    cut = sorted(cut)
    cut = [0] + cut + [length]
    n = len(cut)
    dp = [[0 for i in range(n)] for j in range(n)]
    for gap in range(2, n):
        for left in range(0, n - gap):
            right = left + gap
            dp[left][right] = float('inf')
            for k in range(left + 1, right):
                dp[left][right] = min(dp[left][right], dp[left][k] + dp[k][right] + cut[right] - cut[left])
    return dp[0][n - 1]

print(cutting_stick(length, cut))