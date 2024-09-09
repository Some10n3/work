def f(x):
    return x*x +x

def solve_seq(ans):
    lo = 0
    hi = 1000000000000000000
    while(lo<=hi):
        mid = (hi+lo)//2
        y = f(mid)
        if mid == lo:
            break
        elif ans == y:
            return mid
        elif ans < y:
            hi = mid
        else:
            lo = mid
    return mid
        
inp = int(input(""))
print(solve_seq(inp))