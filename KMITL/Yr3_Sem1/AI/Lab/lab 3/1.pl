fib(0, 0):-!.
fib(1, 1):-!.


fib(N, F) :- 
    N1 is N - 1, 
    fib(N1, F1), 
    N2 is N - 2, 
    fib(N2, F2), 
    F is F1 + F2.

% ?- fib(5, X).