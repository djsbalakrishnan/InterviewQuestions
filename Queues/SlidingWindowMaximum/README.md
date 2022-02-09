## Sliding Window Maximum
Given an array of integers A. There is a sliding window of size B which is moving from the very left of the array to the very right. You can only see the B numbers in the window. Each time the sliding window moves rightwards by one position. You have to find the maximum for each window.
Return an array C, where C[i] is the maximum value in the array from A[i] to A[i+B-1].


### Constraints
```
1 <= |A|, B <= 1e6
```

### Examples
###### Input
```
 A = [1, 3, -1, -3, 5, 3, 6, 7]
 B = 3
```
###### Output
```
 [3, 3, 5, 5, 6, 7]
```
###### Explanation
```
 Window position     | Max
 --------------------|-------
 [1 3 -1] -3 5 3 6 7 | 3
 1 [3 -1 -3] 5 3 6 7 | 3
 1 3 [-1 -3 5] 3 6 7 | 5
 1 3 -1 [-3 5 3] 6 7 | 5
 1 3 -1 -3 [5 3 6] 7 | 6
 1 3 -1 -3 5 [3 6 7] | 7
```
