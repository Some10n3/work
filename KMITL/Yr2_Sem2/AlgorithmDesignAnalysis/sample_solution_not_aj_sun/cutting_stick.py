def cutting_stick( length, cut ):
    middle = length // 2
    closet = 0
    for gap in cut:
        if abs( gap - middle ) < abs( closet - middle ):
            closet = gap
    if closet == 0:
        return 0
    left_cut_list =  [ i for i in cut if i < closet ]
    right_cut_list = [ i - closet for i in cut if i > closet ]


    return length + cutting_stick( closet, left_cut_list ) + cutting_stick(length - closet, right_cut_list )
        
length = int(input(""))
cut = list(map(int, input("").split()))
print(cutting_stick(length, cut))