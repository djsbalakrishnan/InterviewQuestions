## Connect Ropes
Given an array of integers A representing the length of ropes. You need to connect these ropes into one rope. The cost of connecting two ropes is equal to the sum of their lengths. Find and return the minimum cost to connect these ropes into one rope.


#### Constraints
```
1 <= length of the array <= 100000
1 <= A[i] <= 1000
```

###### Example Input
```
 A = [5, 17, 100, 11]
```

###### Example Output
```
 182
```

######
```
 Given array A = [5, 17, 100, 11].
 Connect the ropes in the following manner:
 5 + 11 = 16
 16 + 17 = 33
 33 + 100 = 133

 So, total cost  to connect the ropes into one is 16 + 33 + 133 = 182.
```
