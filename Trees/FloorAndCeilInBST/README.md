## Floor and Ceil in BST
Given a Binary Search Tree rooted at A and an integer array B of size N. Find the floor and ceil of every element of the array B.
Floor(X) is the highest element in the tree <= X, while the ceil(X) is the lowest element in the tree >= X.
NOTE: If floor or ceil of any element of B doesn't exists, output -1 for the value which doesn't exists.

### Constraints
```
0 <= Number of nodes in the tree <= 1e5
0 <= node values <= 1e9
0 <= N <= 1e5
0 <= B[i] <= 1e9
```

### Examples
###### Input
```
Given Tree A:
           10
         /    \
        4      15
       / \
      1   8
B = [4, 19]   
```
###### Output
```
[
    [4, 4]
    [15, -1]
]
```
