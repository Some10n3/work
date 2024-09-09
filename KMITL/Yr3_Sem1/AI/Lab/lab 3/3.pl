drawTree(S, L) :- drawTree(S, L, 0).

drawTree(S, L, I) :- I =< L, I1 is I + 1, drawTree(S, L, I1), drawLine(S, I).

drawTree(S, L, I) :- I =< L, I1 is I + 1, drawTree(S, L, I1).

drawLine(S, I) :- drawLine(S, I, 0).

drawLine(S, I, J) :- J < I, J1 is J + 1, write(S), drawLine(S, I, J1).

drawLine(S, I, J) :- J =:= I, write('\n').

% ?- drawTree('*', 5).