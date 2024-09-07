/*

1.1)  Identifying the operations in the following snippet:

What objects/variables are created in the statement?
ix1, ix2, ix3, ix4, ss1, ss2, ss3, ss4, ss5, ss6

What are their types and values?
ix1: int, value: 20
ix2: int, uninitialized
ix3: function declaration, returns int, takes no arguments
ix4: int, value: 0
ss1: string, value: "****"
ss2: string, value: "&&&"
ss3: string, value: "htm"
ss4: string, value: "x.htm"
ss5: string, empty
ss6: string, value: "x.png"

Count the number of them.
10

What operations are they created?
Default initialization, value initialization, copy initialization.

Are there errors in the statement? Identify and correct them.
The declaration of int ix3() creates a function declaration instead of an integer variable. It should be changed to int ix3 = 0;.

At which statements does the copy assignment happen?
The copy assignment happens at the statement ss1 = ss2 = ss4;.

Which objects are assigned?
ss2 and ss4 are assigned to ss1.

By what value?
ss1 is assigned the value of ss4, which is "x.htm". ss2 is assigned the value of ss4, which is also "x.htm".

*/


/*

1.2) Identifying the operations in the following snippet:

What objects/variables are created in the statement?
num_array, s, vs1, vs2, vs3, vs4, vv1, vv2, vv3

What are their types and values?
num_array: array of doubles, uninitialized
s: string, value: ""
vs1: vector of strings, size: 5, each element initialized to ""
vs2: vector of strings, size: 4, default-initialized to empty strings
vs3: vector of strings, copy-initialized from vs1
vs4: vector of strings, size: 0
vv1: vector of doubles, size: 2, values: {3.0, 2.5}
vv2: vector of doubles, size: 2, default-initialized to 0.0
vv3: vector of doubles, default-initialized to an empty vector

Count the number of them.
9

What operations are they created?
Default initialization, value initialization, copy initialization.

Are there errors in the statement? Identify and correct them.
There are no errors.

At which statements does the copy assignment happen?
The copy assignment happens at the statements vs1 = vs2 = vs3; and vv2 = vv1;.

Which objects are assigned?
In the first statement, vs2 and vs3 are assigned to vs1. In the second statement, vv1 is assigned to vv2.

By what value?
In the first statement, vs1 is assigned the value of vs3, which is a copy of vs1, and vs2 is assigned the value of vs3. In the second statement, vv2 is assigned the value of vv1, which is {3.0, 2.5}.

*/

/*

1.3) Identifying the operations in the following snippet:

What objects/variables are created in the statement?
x_map, vv1, vv2

What are their types and values?
x_map: map of strings to vectors of doubles, size: 1, key: "exp", value: {1.1, 2.2, 3.3}
vv1: vector of doubles, value: {1.1, 2.2, 3.3}
vv2: vector of doubles, uninitialized

Count the number of them.
3

What operations are they created?
Default initialization, value initialization, copy assignment.

Are there errors in the statement? Identify and correct them.
There are no errors in this statement.

At which statements does the copy assignment happen?
The copy assignment happens at the statements vv1 = x_map["exp"]; and vv2 = x_map["exp"];.

Which objects are assigned?
In the first statement, vv1 is assigned the value of the vector associated with the key "exp" in x_map, which is {1.1, 2.2, 3.3}. In the second statement, vv2 is assigned the same value as vv1.

By what value?
In both statements, the value assigned is {1.1, 2.2, 3.3}. In the second statement, since the key "exp" does not exist in x_map, a default-constructed vector is returned and assigned to vv2, which is an empty vector.

*/