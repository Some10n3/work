
house1 = ['yellow', 'norwegian', '', '', 'dunhill']
house2 = ['blue', '', 'horse', '', '']
house3 = ['red', 'brit', '', 'milk', '']
house4 = ['white', '', '', 'coffee', '']
house5 = ['green', '', '', '', '']

houses = [house1, house2, house3, house4, house5]

houses[0][2] = 'cat'
houses[1][4] = 'blend'
houses[2][4] = 'pall mall'
houses[3][1] = 'german'
houses[4][4] = 'blue master'


for i in range(len(houses)):
    if houses[i][1] == "" and houses[i][2] == "":
        if houses[i - 1][1] == "Swede" and houses[i - 1][2] == "Dogs":
            continue
        else:
            houses[i][1] = "Swede"
            houses[i][2] = "Dogs"
    if houses[i][1] == "" and houses[i][3] == "":
        houses[i][1] = "Dane"
        houses[i][3] = "Tea"
    if houses[i - 1][4] == "Pall Mall" and houses[i - 1][2] == "":
        houses[i - 1][2] = "Birds"
    if houses[i - 1][4] == "Blue Master" and houses[i - 1][3] == "":
        houses[i - 1][3] = "Beer"
    if houses[i - 1][1] == "German" and houses[i - 1][4] == "":
        houses[i - 1][4] = "Prince"
    if houses[i - 1][2] == "Cats" and houses[i][4] == "":
        houses[i][4] = "Blends"
    if houses[i - 1][4] == "Blends" and houses[i][2] == "":
        houses[i - 1][2] = "Cats"
    if houses[i][4] == "Blends" and houses[i - 1][3] == "" and houses[i + 1][3] != "":
        houses[i - 1][3] = "Water"
    if houses[i][4] == "Blends" and houses[i + 1][3] == "" and houses[i - 1][3] != "":
        houses[i + 1][3] = "Water"

print('\n')
print("Attributes of each house")
for i in range(len(houses)):
    print(f"house{i} = {houses[i][0]}, {houses[i][1]}, {houses[i][2]}, {houses[i][3]}, {houses[i][4]}")

print('\n')
print("Answer:", end='')
for i in range(len(houses)):
    if houses[i][2] == "":
        houses[i][2] = "Fish"
        print(f"house{i + 1} have {houses[i][2]} as a pet!")