foods = []

while True:
    n = int(input())
    if n == 0:
        break
    
    x = {}
    for i in range(int(n)):
        N = input()
        N = N.split(" ")
        for j in range(len(N)):
            if j > 0:
                if N[j] not in x:
                    x[N[j]] = []
                x[N[j]].append(N[0])
    foods.append(x)

for case in foods:
    for food in sorted(case):
        print(food, end=" ")
        for name in sorted(case[food]):
            print(name, end=" ")
        print()
    print()