numberset = input("").split()
numberset = [int(i) for i in numberset]

def numberpicking(numberset):
    if len(numberset) == 0:
        return "No"
    if len(numberset) == 1:
        return "Yes"
    if len(numberset) == 2:
        if abs(numberset[0] - numberset[1]) <=9 :
            return "Yes"
        else:
            return "No"

    while len(numberset) > 0:
        newset = numberset
        if (abs(numberset[0] - numberset[1]) <=9 or abs(numberset[0]-numberset[-1]) <=9) and (abs(numberset[-1] - numberset[0]) <=9 or abs(numberset[-2]-numberset[-1]) <=9):
                now = newset.copy()
                now.pop(0)
                while len(now) > 1:
                    if (abs(now[0] - now[1]) <=9 or abs(now[0]-now[-1]) <=9) :
                        now.pop(0)
                    elif (abs(now[-1] - now[0]) <=9 or abs(now[-2]-now[-1]) <=9) :
                        now.pop(-1)
                    else:
                        newset.pop(-1)
                        while len(numberset) > 1:
                            if (abs(numberset[0] - numberset[1]) <=9 or abs(numberset[0]-numberset[-1]) <=9) :
                                newset.pop(0)
                            elif (abs(numberset[-1] - numberset[0]) <=9 or abs(numberset[-2]-numberset[-1]) <=9) :
                                newset.pop(-1)
                            else:
                                return "No"
                        return "Yes"
                return "Yes"
        elif (abs(numberset[0] - numberset[1]) <=9 or abs(numberset[0]-numberset[-1]) <=9) :
            newset.pop(0)
        elif (abs(numberset[-1] - numberset[0]) <=9 or abs(numberset[-2]-numberset[-1]) <=9) :
            newset.pop(-1)
        else:
            return "No"
        
    return "Yes" 
    

print(numberpicking(numberset))