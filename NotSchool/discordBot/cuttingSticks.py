#recurssive solution to the cutting sticks problem with memoization
def cuttingSticks(arr, l, r, memo):
    if l + 1 == r: return 0
    if memo[l][r] != -1: return memo[l][r]
    ans = float('inf')
    for i in range(l + 1, r):
        ans = min(ans, cuttingSticks(arr, l, i, memo) + cuttingSticks(arr, i, r, memo) + arr[r] - arr[l])
    memo[l][r] = ans
    return ans

def main():
    length = int(input("len :"))
    cuts = input("cuts :").split()
    cuts = [int(cut) for cut in cuts]
    cuts = [0] + cuts + [length]
    memo = [[-1 for c in range(len(cuts))] for c in range(len(cuts))]
    print(cuttingSticks(cuts, 0, len(cuts) - 1, memo))

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

def main_bottom_up():
    length = int(input("len :"))
    cuts = input("cuts :").split()
    cuts = [int(cut) for cut in cuts]
    cuts = [0] + cuts + [length]
    print(cuttingSticks_bottom_up(cuts))

def optimal_cutting_sticks(P):
    N = len(P)
    opt_profit = [0] * (N + 1)
    opt_cuts = [[] for _ in range(N + 1)]

    opt_profit[1] = P[0]
    opt_cuts[1] = []

    for n in range(2, N + 1):
        max_profit = P[n - 1]
        max_cuts = []

        for k in range(1, n):
            if max_profit < P[k - 1] + opt_profit[n - k]:
                max_profit = P[k - 1] + opt_profit[n - k]
                max_cuts = [k] + opt_cuts[n - k]

        opt_profit[n] = max_profit
        opt_cuts[n] = max_cuts

    print("Optimal Profit:", opt_profit[N])
    print("Optimal Cuts:", opt_cuts[N])

def main_optimal_cutting_sticks():
    length = int(input("len :"))
    cuts = input("cuts :").split()
    cuts = [int(cut) for cut in cuts]
    cuts = cuts + [length]
    print(cuts)
    print(optimal_cutting_sticks(cuts))
    

if __name__ == "__main__":
    # main()
    # main_bottom_up()
    main_optimal_cutting_sticks()