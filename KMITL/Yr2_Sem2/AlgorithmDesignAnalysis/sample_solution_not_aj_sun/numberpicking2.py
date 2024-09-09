inp = input()

def picking_number(list_input, number):
    length = len(list_input)
    # print(list_input)
    if abs(number - list_input[0]) > 9 and abs(number - list_input[length-1]) > 9:
        return 0
    elif length == 1:
        return 1
    else:
        if abs(number - list_input[0]) <= 9 and abs(number - list_input[length-1]) <= 9:
            return picking_number(list_input[1:], list_input[0]) or picking_number(list_input[:length-1], list_input[length-1])
        
        elif abs(number - list_input[0]) <= 9:
            return picking_number(list_input[1:], list_input[0])
        
        else:
            return picking_number(list_input[:length-1], list_input[length-1])

if inp == "":
    print("No")
else:
    inp = inp.split(" ")
    inp = [int(i) for i in inp]
    if picking_number(inp, inp[0]) or picking_number(inp, inp[len(inp)-1]):
        print("Yes")
    else:
        print("No")