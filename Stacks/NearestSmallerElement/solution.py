class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        nsl = [-1]
        stack = []
        stack.append(A[0])
        
        for i in range(1, len(A)):
            ele = A[i]
            while len(stack) > 0 and A[i] <= stack[len(stack)-1]:
                stack.pop()            
            if len(stack) > 0:
                nsl.append(stack[len(stack)-1])
            else:
                nsl.append(-1)
            stack.append(ele)
        
        return nsl
