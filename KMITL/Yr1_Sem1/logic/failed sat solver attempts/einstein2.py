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


# S will be used to store the list of the clauses to be constructed
S = []

# Generate clauses for each condition of 2x2 sudoku game
# 1. Each cell contains a single number, 1-4.
for i in range(1,6):
    for j in range(1,6):
        # Cell (i,j) contains at least one of the numbers 1-4
        S.append([p(i,j,k) for k in range(1,26)])

# 2. Each row must contain all numbers 1-4.
for i in range(1,6):
    for j in range(1,6):
        # Row i must contain number k
        S.append([p(j,i,k) for k in range(1,26)])

# 5. Initial numbers
S.append([p(3,4,18)])
S.append([p(1,2,9)])
S.append([p(2,1,5)])

# Check for satisfiability
result = sat(S)

print(result)