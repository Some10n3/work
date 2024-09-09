def boothrental(fee, days):
    profit = [d - fee for d in days]
    max_profit = 0
    for i in range(len(profit)):
        for j in range(0, i):
            max_profit = max(max_profit, sum(profit[j:i]))
    return max_profit if max_profit > 0 else "No"


def main() :
    fee = int(input(""))
    days = (input("")).split(" ")
    days = [int(i) for i in days]
    print(boothrental(fee, days))
    
main()
