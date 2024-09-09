S = [3, 7, 5, 1, 4]

memo = {}
def check(k, Y):
    if k == 0:
        return Y == 0
    else:
        if (k, Y) in memo:
            return memo[(k, Y)]
        elif Y >= S[k - 1]:
            memo[(k, Y)] = check(k-1, Y-S[k - 1]) or check(k-1, Y)
            return memo[(k, Y)]
        else:
            memo[(k, Y)] = check(k-1, Y)
            return memo[(k, Y)]

def check_bottom_up(k, Y):
    check = [[False for _ in range(Y + 1)] for _ in range(k + 1)]
    check[0][0] = True

    for i in range(1, k + 1):
        print(check[i])
        print()

    for i in range(1, k + 1):
        for j in range(Y + 1):
            if j >= S[i - 1]:
                check[i][j] = check[i - 1][j - S[i - 1]] or check[i - 1][j]
            else:
                check[i][j] = check[i - 1][j]

    print()
    for i in range(1, k + 1):
        print(check[i])
        print()

    return check[k][Y]

# print(check(0, 0))
# print(check(5, 6))
print(check_bottom_up(5, 6))