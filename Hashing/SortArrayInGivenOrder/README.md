## Sort Array in given Order
Given two array of integers A and B, Sort A in such a way that the relative order among the elements will be the same as those are in B. For the elements not present in B, append them at last in sorted order.

Return the array A after sorting from the above method.
NOTE: Elements of B are unique.

### Constraints
```
1 <= length of the array A <= 1e5
1 <= length of the array B <= 1e5
-10^9 <= A[i] <= 10^9 
```

### Examples
###### Input
```
A = [1, 2, 3, 4, 5]
B = [5, 4, 2]
```
###### Output
```
[5, 4, 2, 1, 3]
```
###### Explanation
```
Simply sort as described.
```