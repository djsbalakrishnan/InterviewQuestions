## BST Nodes in a Range
Given a binary search tree of integers. You are given a range B and C.
Return the count of the number of nodes that lies in the given range.

### Constraints
```
1 <= Number of nodes in binary tree <= 1e5
0 <= B < = C <= 1e9 
```

### Examples
###### Input
```
            15
          /    \
        12      20
        / \    /  \
       10  14  16  27
      /
     8

     B = 12
     C = 20

```
###### Output
```
 5
```

###### Explanation 
```
 Nodes which are in range [12, 20] are : [12, 14, 15, 20, 16]
```
