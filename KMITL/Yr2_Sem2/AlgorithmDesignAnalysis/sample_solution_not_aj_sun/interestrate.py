inp1 = float(input(""))
inp2 = float(input(""))
inp3 = float(input(""))

def interest_rate(rate, one, two, three):
    return one * rate ** 3 + two * rate ** 2 + three * rate

def highest_profit(a, b, c):
    max_profit = 0
    max_rate = 0.0
    for i in range(0, 2001, 1):
        i = i/100.0
        if interest_rate(i, a, b, c) > max_profit:
            max_profit = interest_rate(i, a, b, c)
            max_rate = i
            
    return max_rate

print(highest_profit( inp1, inp2, inp3))