##  Kth Smallest Element in a Sorted Matrix
Given a sorted matrix of integers A of size N x M and an integer B. Each of the rows and columns of matrix A are sorted in ascending order, find the Bth smallest element in the matrix.

NOTE: Return The Bth smallest element in the sorted order, not the Bth distinct element.


#### Constraints
```
1 <= N, M <= 500
1 <= A[i] <= 1e9
1 <= B <= N * M
```

###### Example Input
```
  A = [  [5, 9, 11],
        [9, 11, 13],
        [10, 12, 15],
        [13, 14, 16],
        [16, 20, 21] ]
 B = 12
```

###### Example Output
```
 16
```

######
```
 12th smallest element in the sorted matrix is 16.
```
