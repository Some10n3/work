%Facts
male(john).
male(oliver).
male(ali).
male(james).
male(jack).
male(harry).

female(helen).
female(sophie).
female(mary).
female(sue).

parent(john, mary).
parent(john, sue).
parent(helen, mary).
parent(helen, sue).
parent(oliver, james).
parent(sophie, james).
parent(mary, jack).
parent(ali, jack).
parent(sue, harry).
parent(james, harry).

%Rule
father(X, Y):- male(X), parent(X, Y).
mother(X, Y):- female(X), parent(X, Y).
grandfather(X, Y):- father(X, Z), parent(Z, Y).
grandmother(X, Y):- mother(X, Z), parent(Z, Y).
sibling(X, Y):- parent(Z, X), parent(Z, Y), X \= Y.
sister(X, Y):- parent(Z, X), parent(Z, Y), Y \= X.
brother(X, Y):- parent(Z, X), parent(Z, Y).
uncle(X, Y):- brother(X, Z), parent(Z, Y).
aunt(X, Y):- sister(X, Z), parent(Z, Y).

%Queries
% who is a sister of mary and who ar there parents?
%   sister(X, mary), parent(Y, mary).
% who has a parent
%   parent(_, X).
% who is a child of somebody
%   parent(_, X).
% who is a sister of somebody
%   sister(X, _).

