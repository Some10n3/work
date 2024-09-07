s = input()
s = s.split(" ")
#prints percentage that is cheese

radius = int(s[0])
crust = int(s[1])

if radius == 1 and crust == 1:
    print("0.000000")
else:
    cheese = (radius - crust)**2
    total = radius**2
    percent = (cheese/total) * 100
    print("{0:.6f}".format(percent))