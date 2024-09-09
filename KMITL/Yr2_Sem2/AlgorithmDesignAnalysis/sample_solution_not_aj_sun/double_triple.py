def shorteststep(number ):
    step = 0
    substep = 0
    new = 1
    while new != number:
        if new * 3 < number:
            new *=3
            step +=1
        elif new * 2 < number:
            new *=2
            step +=1
        else:
            new +=1
            step +=1
    return step


mynum = int(input(""))
print(shorteststep(mynum ))