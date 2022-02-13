## Left View Of Binary Tree
Given a binary tree of integers. Return an array of integers representing the left view of the Binary tree. Left view of a Binary Tree is a set of nodes visible when the tree is visited from Left side

NOTE: The value comes first in the array which have lower level.

### Constraints
```
1 <= Number of nodes in binary tree <= 1e5
0 <= node values <= 1e9
```

### Examples
###### Input
```
            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8 
```
###### Output
```
 [1, 2, 4, 8]
```
###### Explanation
```
 The Left view of the binary tree is returned.
```
