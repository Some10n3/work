
```
% Facts: parent relationships
parent(john, mary).
parent(john, mark).
parent(mary, alice).
parent(mary, bob).
parent(mark, tom).
parent(alice, sue).
parent(bob, jane).
parent(sue, jill).
parent(jane, jack).

% Facts: age of each person
age(john, 70).
age(mary, 50).
age(mark, 52).
age(alice, 30).
age(bob, 28).
age(tom, 25).
age(sue, 18).
age(jane, 20).
age(jill, 5).
age(jack, 2).
```

```
% Rule: ancestor relationship (recursive)
ancestor(X, Y) :-
    parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).

% Rule: sibling relationship
sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

```

```
Output :
| ?- findall(Ancestor, ancestor(Ancestor, jill), Ancestors).
findall(Ancestor, ancestor(Ancestor, jill), Ancestors).
Ancestors = [sue,john,mary,alice]

yes
| ?- 
```


Here's a step-by-step breakdown of how Prolog processes the `ancestor/2` query using recursion:

1. **First Ancestor Rule (`ancestor(X, Y) :- parent(X, Y).`)**:
   - Prolog checks if `jill` has a direct parent. It finds `parent(sue, jill)`, so it matches `ancestor(sue, jill)`.
   - `sue` is thus recorded as one of `jill`'s ancestors.

2. **Second Ancestor Rule (`ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).`)**:
   - Prolog now looks for additional ancestors by checking if `jill` has an ancestor through intermediate relationships.
   - It finds that `sue` is a parent of `jill`, so it searches for `sue`'s parent. It finds `parent(alice, sue)`, so `ancestor(alice, jill)` is true.
   - This process repeats: Prolog finds `alice`'s parent `mary`, making `ancestor(mary, jill)` true, and then `mary`'s parent `john`, making `ancestor(john, jill)` true.

3. **Recursive Backtracking**:
   - Prolog keeps backtracking to find all possible ancestors by tracing the `parent` chain upward until no more parents are found.
   - As a result, it gathers all ancestors of `jill` in the list: `[sue, john, mary, alice]`.

Using the recursive rule allows Prolog to traverse each level up the family tree, collecting ancestors without having to explicitly define multiple layers of relationships. This recursive structure is powerful for working with hierarchical data, as seen here.