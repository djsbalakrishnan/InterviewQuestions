## MAX and MIN 
Given an array of integers A .
value of a array = max(array) - min(array).
Calculate and return the sum of values of all possible subarrays of A % 1e9+7.

### Constraints
```
1 <= |A| <= 1e5
1 <= A[i] <= 1e7
```

### Examples
```
Input: A = [4, 7, 3, 8]
Output: 26
```
##### Explanation
```
value ( [4] ) = 4 - 4 = 0
value ( [7] ) = 7 - 7 = 0
value ( [3] ) = 3 - 3 = 0
value ( [8] ) = 8 - 8 = 0
value ( [4, 7] ) = 7 - 4 = 3
value ( [7, 3] ) = 7 - 3 = 4
value ( [3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3] ) = 7 - 3 = 4
value ( [7, 3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3, 8] ) = 8 - 3 = 5
sum of values % 1e9+7 = 26
```
