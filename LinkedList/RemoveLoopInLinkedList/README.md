## Remove Loop in Linked List 
Given a linked list which contains some loop.
You need to find the node, which creates a loop, and break it by making the node point to NULL.

#### Constraints
`1 <= N <= 1e3`

#### Example Input
`3 -> 2 -> 4 -> 5 -> 6`
          `^         |`
          `|         |`    
          `- - - - - -`

#### Example Output
`3 -> 2 -> 4 -> 5 -> 6 -> NULL`
