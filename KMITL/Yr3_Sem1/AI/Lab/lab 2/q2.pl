connection(boston, new_york).
connection(new_york, philadelphia).
connection(philadelphia, washington).
connection(washington, atlanta).
connection(washington, new_york).

path(x, y) :- connection(x, y).
path(x, y) :- connection(x, z), path(z, y).