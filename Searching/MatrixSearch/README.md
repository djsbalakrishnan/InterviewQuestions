## Matrix Search
Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that searches for integar B in matrix A.

This matrix A has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than or equal to the last integer of the previous row.

Return 1 if B is present in A, else return 0. 

### Constraints
```
1 <= N, M <= 1000
1 <= A[i][j], B <= 1e6
```

### Examples
###### Input
```
A = [ 
      [1,   3,  5,  7]
      [10, 11, 16, 20]
      [23, 30, 34, 50]  
    ]
B = 3
```
###### Output
```
1
```