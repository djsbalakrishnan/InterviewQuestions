## Contiguous Array
Given an array of integers A consisting of only 0 and 1.
Find the maximum length of a contiguous subarray with equal number of 0 and 1.

### Constraints
```
1 <= length of the array <= 1e5
0 <= A[i] <= 1
```

### Examples
###### Input
```
A = [1, 0, 1, 0, 1]
```
###### Output
```
4
```
###### Explanation
```
Subarray from index 0 to index 3 : [1, 0, 1, 0]
Subarray from index 1 to index 4 : [0, 1, 0, 1]
Both the subarrays have equal number of ones and equal number of zeroes.
```