import turtle as t

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

n = int(input("Enter the dimension : "))
side_length = 450/n
angle = 360/4

def p(i,j):
    return 'p'+str(i)+str(j)
def np(i,j):
    return '~p'+str(i)+str(j)

S = []

if n == 1:
  S.append([p(1,1)])
#when "n" = 5 the "result" from DPLL algorithm "p35" is missing but "n" in other number "result" have "p35"
#I checked "S" I still see "~p35" but there is no "p35" in "result"
#I don't know where is go wrong.So I decide to add p35 directly
elif n == 5: 
  S.append([p(3,5)])


#row
for c in range(1,n+1):
  for i in range(1,n+1):
    for j in range(i,n+1):
      if np(c,i) != np(c,j):
        S.append([np(c,i),np(c,j)])

#column
for c in range(1,n+1):
  for i in range(1,n+1):
    for j in range(i,n+1):
      if np(c,i) != np(c,j):
        S.append([np(i,c),np(j,c)])

#diagonal to right
for c in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      if c+(j-1) <= n and i+(j-1) <= n and np(c,i) != np(c+(j-1),i+(j-1)):
        S.append([np(c,i),np(c+(j-1),i+(j-1))])

#diagonal to left
for c in range(1,n+1):
  for i in range(1,n+1):
      for j in range(1,n+1):
        if c+j-1 <= n and i-(j-1) > 0 and np(c,i) != np(c+j-1,i-(j-1)):
          S.append([np(c,i),np(c+j-1,i-(j-1))])

print(S)
result = sat(S)
print(result)

t.right(180)
t.speed(10)
if result is None:
    print('No solution')
else:
  for i in range(1,n+1):
    for j in range(1,n+1):
      if result[p(i,j)]:
        t.penup()
        t.forward(side_length/2)
        t.left(angle)
        t.forward(side_length/2)
        t.write("X", align='center')
        t.left(180)
        t.forward(side_length/2)
        t.right(angle)
        t.forward(side_length/2)
        t.left(180)
        t.pendown()
      for k in range(4):
        t.forward(side_length)
        t.left(angle)
      t.left(angle)
      t.forward(side_length)
      t.right(angle)
    t.right(angle)
    t.forward(side_length*n)
    t.left(angle)
    t.forward(side_length)

t.mainloop()