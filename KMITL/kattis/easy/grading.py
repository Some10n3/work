criteria = input()
score = int(input())

criteria = criteria.split(" ")

if score >= int(criteria[0]):
    print("A")
elif score >= int(criteria[1]):
    print("B")
elif score >= int(criteria[2]):
    print("C")
elif score >= int(criteria[3]):
    print("D")
else:
    print("F")