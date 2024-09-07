input_list = []

for i in range(2):
    N = input()
    input_list.append(N)
    
hr = int(input_list[0])
min = int(input_list[1])

if min - 45 < 0:
    min = min + 15  
    if hr == 0:
        hr = 23
    else:
        hr -= 1 
else:
    min = min - 45
    
s = str(hr)
s += " "
s += str(min)

print(s)
