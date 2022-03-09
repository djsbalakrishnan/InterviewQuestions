## Running Median
Given an array of integers A denoting a stream of integers. New arrays of integer B and C are formed. Each time an integer is encountered in a stream, append it at the end of B and append median of array B at the C.

Find and return the array C.

NOTE:
- If the number of elements are N in B and N is odd then consider medain as B[N/2] ( B must be in sorted order).
- If the number of elements are N in B and N is even then consider medain as B[N/2-1]. ( B must be in sorted order).

#### Constraints
```
1 <= N <= 1e5
0 <= A[i] <= INT_MAX
```

###### Example Input
```
 A = [5, 17, 100, 11]
```

###### Example Output
```
 [5, 5, 17, 11]
```

###### Explanation
```
 stream          median
 [5]              5
 [5, 17]          5
 [5, 17, 100]     17
 [5, 17, 100, 11] 11 
```
