## Common Nodes in Two BST
Given two BST's A and B, return the sum of all common nodes in both A and B % (1e9 +7) .
In case there is no common node, return 0.

### Constraints
```
1 <= Number of nodes in binary tree <= 1e5
0 <= node values <= 1e6
```

### Examples
###### Input
```
 Tree A:
    5
   / \
  2   8
   \   \
    3   15
        /
        9

 Tree B:
    7
   / \
  1  10
   \   \
    2  15
       /
      11        
```
###### Output
```
 17
```

###### Explanation
```
 Common Nodes are : 2, 15
 So answer is 2 + 15 = 17
```
