## Wave Array
Given an array of integers A, sort the array into a wave-like array and return it.
In other words, arrange the elements into a sequence such that

```
a1 >= a2 <= a3 >= a4 <= a5..... 
```

NOTE: If multiple answers are possible, return the lexicographically smallest one.

### Constraints
```
1 <= len(A) <= 1e6
1 <= A[i] <= 1e6
```

### Examples
###### Input
```
A = [1, 2, 3, 4]
```
###### Output
```
[2, 1, 4, 3]
```

###### Input
```
A = [1, 2]
```
###### Output
```
[2, 1]
```