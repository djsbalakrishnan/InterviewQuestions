## Recover Binary Search Tree
Two elements of a binary search tree (BST),represented by root A are swapped by mistake. Tell us the 2 values swapping which the tree will be restored.
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution? 


### Constraints
```
1 <= Number of nodes in binary tree <= 1e5
```

### Examples
###### Input
```
     1
    / \
   2   3
```
###### Output
```
  [2, 1]
```

###### Explanation 
```
Swapping 1 and 2 will change the BST to be 
         2
        / \
       1   3
which is a valid BST 
```
