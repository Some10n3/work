sum_list([], 0).

sum_list([H|T], S) :- sum_list(T, S1), S is H + S1.