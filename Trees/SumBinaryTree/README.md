## Sum Binary Tree or Not
Given a binary tree. Check whether the given tree is a Sum-binary Tree or not.
Sum-binary Tree is a Binary Tree where the value of a every node is equal to sum of the nodes present in its left subtree and right subtree.
An empty tree is Sum-binary Tree and sum of an empty tree can be considered as 0. A leaf node is also considered as SumTree.
Return 1 if it sum-binary tree else return 0.


### Constraints
```
1 <= Number of nodes in binary tree <= 1e5
0 <= node values <= 50
```

### Examples
###### Input
```
       26
     /    \
    10     3
   /  \     \
  4   6      3
```
###### Output
```
1
```
###### Explanation
```
 All leaf nodes are considered as SumTree. 
 Value of Node 10 = 4 + 6.
 Value of Node 3 = 0 + 3 
 Value of Node 26 = 20 + 6 
```
