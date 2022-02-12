## Count Right Triangles
Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2D Cartesian plane.

Find and return the number of unordered triplets (i, j, k) such that (A[i], B[i]), (A[j], B[j]) and (A[k], B[k]) form a right angled triangle with the triangle having one side parallel to the x-axis and one side parallel to the y-axis.

NOTE: The answer may be large so return the answer modulo (109 + 7).

### Constraints
```
1 <= N <= 1e5
0 <= A[i], B[i] <= 1e9 
```

### Examples
###### Input
```
 A = [1, 1, 2, 3, 3]
 B = [1, 2, 1, 2, 1]
```
###### Output
```
6
```
###### Explanation
```
6 quadruplets which make a right angled triangle are: (1, 1), (1, 2), (2, 1)
                                                      (1, 1), (3, 1), (1, 2)
                                                      (1, 1), (3, 1), (3, 2)
                                                      (2, 1), (3, 1), (3, 2)
                                                      (1, 1), (1, 2), (3, 2)
                                                      (1, 2), (3, 1), (3, 2)
```