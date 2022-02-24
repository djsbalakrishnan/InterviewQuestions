## Serialize Binary Tree
Given the root node of a Binary Tree denoted by A. You have to Serialize the given Binary Tree in the described format.
Serialize means encode it into a integer array denoting the Level Order Traversal of the given Binary Tree.

NOTE:
- In the array, the NULL/None child is denoted by -1.
- For more clarification check the Example Input.

#### Constraints
```
1 <= number of nodes <= 1e5
```

#### Example Input
```
           1
         /   \
        2     3
       / \
      4   5
```

#### Example Output
```
 [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]
```
