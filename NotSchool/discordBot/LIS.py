def longestIncreasingSubsequence(arr):
    lenn = len(arr)
    
    if lenn == 0:
        return 0

    if lenn == 1:
        return 1

    dp = [1] * lenn

    for i in range(1, lenn):
        for j in range(0, i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1

    return max(dp)

# 4 10 2 1 20
# i = 4
# j = 3
# dp[1, 2, 1, 1, 3]

# 1 - [4, 10]
# 4 - [4, 20]
# 4 - [10,20]
# 4 - [2, 20]
# 4 - [1, 20]


if __name__ == "__main__":
    user_input = input().split()
    arr = [int(x) for x in user_input]
    print(longestIncreasingSubsequence(arr))