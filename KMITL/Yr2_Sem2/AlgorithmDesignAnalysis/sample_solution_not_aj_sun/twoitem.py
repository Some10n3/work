inp = int(input(""))
item = input("").split()
item =[int(i ) for i in item]

def twoitem(inp, item):
    item = sorted(item )
    mid = len(item ) // 2
    if item[mid ] > inp:
        item = item[:mid ]
    x = 0
    y = len(item)-1
    
    
    while x != y:
        if item[x]+ item[y] == inp:
            return "Yes"
        if item[x]+ item[y] < inp:
            x += 1
        if item[x]+ item[y] > inp:
            y -= 1
    return "No"
        
    # for i in item:
    #     for j in item:
    #         if i + j ==inp and i != j:
    #             return "Yes"
    # return "No"

print(twoitem(inp, item))