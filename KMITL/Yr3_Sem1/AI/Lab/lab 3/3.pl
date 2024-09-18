% Base case: A tree of size 0 has no steps
drawTree(0, []).

% Recursive case: Generate drawing steps for a tree of size S
drawTree(S, [lt(90), fd(S) | RestSteps]) :-
    S > 0,
    S1 is S * 0.7,  % Reduce the size for the next level
    drawBranch(S1, RestSteps).

% Helper predicate to draw branches and recursive calls
drawBranch(0, []) :- !.

drawBranch(S, [lt(30), fd(S), lt(30) | RestSteps]) :-
    S > 0,
    S1 is S * 0.7,  % Reduce the size for the next level
    drawBranch(S1, Steps1),
    append(Steps1, [rt(60), fd(S1), lt(30), backward(S1), lt(30) | Steps2], RestSteps),
    drawBranch(S1, Steps2), !.
