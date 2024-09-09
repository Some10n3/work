isPrime(N) :- N < 2, !, fail.
isPrime(N) :- isPrime(N, 2).

isPrime(N, I) :- I > N / 2, !.
isPrime(N, I) :- N mod I =\= 0, I1 is I + 1, isPrime(N, I1).

% ?- isPrime(5).