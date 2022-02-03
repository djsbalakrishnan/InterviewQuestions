## Min Stack

```
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.
```
```
NOTE:

    All the operations have to be constant time operations.
    getMin() should return -1 if the stack is empty.
    pop() should return nothing if the stack is empty.
    top() should return -1 if the stack is empty.

```

### Constraints
```
1 <= Number of Function calls <= 1e7
```

### Examples 
##### Input 1:
```
push(1)
push(2)
push(-2)
getMin()
pop()
getMin()
top()
```

##### Output 1:
```
-2 1 2
```

##### Input 2:
```
getMin()
pop()
top()
```

##### Output 2:
`-1 -1`
