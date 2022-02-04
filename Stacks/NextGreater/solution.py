class Solution:
    def nextGreater(self, A):
        ngr = [-1]
        stack = [A[len(A)-1]] 
        for i in range(len(A)-2, -1,-1):
            ele = A[i]
            while len(stack) > 0 and ele >= stack[len(stack)-1]:
                stack.pop()
            if len(stack) > 0:
                ngr.insert(0, stack[len(stack)-1])
            else:
                ngr.insert(0, -1)
            stack.append(A[i])
        return ngr
