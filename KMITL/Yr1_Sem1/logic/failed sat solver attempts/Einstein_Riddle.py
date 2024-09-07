### A simple implementation of DPLL algorithm

# Check whether 'clause' contains complementary literals
def tautology(clause):
    for lit in clause:
        neg_lit = '~'+lit if lit[0]!='~' else lit[1:]
        if neg_lit in clause:
            return True
    return False

# Apply simple DPLL algorithm to check satisfiability
def sat(cnf):
    # Empty clause exists means unsatisfiable
    if [] in cnf:
        return None
    
    # Remove tautologies
    new_cnf = [c for c in cnf if not tautology(c)]

    # Empty set of clauses is obviously satisfiable
    if len(new_cnf) == 0:
        return {}

    # Select a propositional letter
    lit = new_cnf[0][0]
    p = lit if lit[0]!='~' else lit[1:]
      
    # Try p true
    new_cnf_p = [c for c in new_cnf if p not in c]
    new_cnf_p = [[l for l in c if l!='~'+p] for c in new_cnf_p]
    result = sat(new_cnf_p)
    if result is not None:
        result[p] = True
        return result
    else:
        # Try p false
        new_cnf_notp = [c for c in new_cnf if '~'+p not in c]
        new_cnf_notp = [[l for l in c if l!=p] for c in new_cnf_notp]
        result = sat(new_cnf_notp)
        if result is not None:
            result[p] = False
            return result
        else:
            return None

def p(i,j,k):
    return 'p'+str(i)+str(j)+str(k)
def np(i,j,k):
    return '~p'+str(i)+str(j)+str(k)

#The man living in the center house drinks milk.
    #center -> milk P318
#The Norwegian lives in the first house.
    #first -> norwegian P109
#The Norwegian lives next to the blue house.
    #second -> blue p205

#The Brit lives in the red house.
#red -> brit 
#The owner of the green house drinks coffee.
#coffee -> green
#The Swede keeps dogs as pets.
#dog -> swede
#The Dane drinks tea.
#tea -> dane
#The person who smokes Pall Mall rears birds.
#bird -> pall mall
#The owner of the yellow house smokes Dunhill.
#dunhill -> yellow
#The man who smokes Blue Master drinks beer.
#beer -> bluemaster
#The German smokes Prince.
#prince -> german

#The green house is on the right of the white house, next to each other.
#
#The man who smokes Blends lives next to the one who keeps cats.
#
#The man who keeps horses lives next to the man who smokes Dunhill.
#
#The man who smokes Blends has a neighbour who drinks water.
#

color = [['red', '01'], ['white', '02'], ['green', '03'], ['yellow', '04'], ['blue', '05']]
nat = [[], [], [], [], []]
pet = [[], [], [], [], []]
drink = [[], [], [], [], []]
cigg = [[], [], [], [], []]

house1 = ['', 'norwegian', '', '', '']
house2 = ['blue', '', '', '', '']
house3 = ['', '', '', 'milk', '']
house4 = ['', '', '', '', '']
house5 = ['', '', '', '', '']

houses = [house1, house2, house3, house4, house5]


for c in range(1, 6):
  for i in range(1, 6):
    for j in range(i, 6):
      if np(c,i) != np(c,j):
        S.append([np(c,i),np(c,j)])










for x in range(len(houses))

for x in range(len(houses)):
    if houses[x][0] == "" and houses[x][1] == "":
        if houses[x - 1][0] == "red" and houses[x - 1][1] == "brit":
            continue
        else:
            houses[x][0] = "red"
            houses[x][1] = "brit"
    


for i in range(len(arr)):
    if arr[i].getNationality() == "" and arr[i].getPet() == "":
        if arr[i - 1].getNationality() == "Swede" and arr[i - 1].getPet() == "Dogs":
            continue
        else:
            arr[i].addNationality("Swede")
            arr[i].addPet("Dogs")
    if arr[i].getNationality() == "" and arr[i].getDrinks() == "":
        arr[i].addNationality("Dane")
        arr[i].addDrinks("Tea")
    if arr[i - 1].getCigBrand() == "Pall Mall" and arr[i - 1].getPet() == "":
        arr[i - 1].addPet("Birds")
    if arr[i - 1].getCigBrand() == "Blue Master" and arr[i - 1].getDrinks() == "":
        arr[i - 1].addDrinks("Beer")
    if arr[i - 1].getNationality() == "German" and arr[i - 1].getCigBrand() == "":
        arr[i - 1].addCigBrand("Prince")
    if arr[i - 1].getPet() == "Cats" and arr[i].getCigBrand() == "":
        arr[i].addCigBrand("Blends")
    if arr[i - 1].getCigBrand() == "Blends" and arr[i].getPet() == "":
        arr[i - 1].addPet("Cats")
    if arr[i].getCigBrand() == "Blends" and arr[i - 1].getDrinks() == "" and arr[i + 1].getDrinks() != "":
        arr[i - 1].addDrinks("Water")
    if arr[i].getCigBrand() == "Blends" and arr[i + 1].getDrinks() == "" and arr[i - 1].getDrinks() != "":
        arr[i + 1].addDrinks("Water")
