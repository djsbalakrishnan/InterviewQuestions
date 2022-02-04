class Solution:
    def NSL(self, A):
        nsl = [-1]
        stack = [0]
        for i in range(1, len(A)):
            ele = A[i]
            while len(stack) > 0 and (ele <= A[stack[len(stack)-1]]):
                stack.pop()
            if len(stack) > 0:
                nsl.append(stack[len(stack)-1])
            else:
                nsl.append(-1)
            stack.append(i)
        
        return nsl
    
    def NSR(self, A):
        nsr = [len(A)]*len(A)
        stack = [len(A)-1] 
        for i in range(len(A)-2, -1,-1):
            ele = A[i]
            while len(stack) > 0 and ele <= A[stack[len(stack)-1]]:
                stack.pop()
            if len(stack) > 0:
                nsr[i] = stack[len(stack)-1]
            else:
                nsr[i] = len(A)
            stack.append(i)

        return nsr

	def largestRectangleArea(self, A):
        # area = base x height
        max_area = -1e9-7
        nsr = self.NSR(A)
        nsl = self.NSL(A)

        for i in range(len(A)):
            height = A[i]
            base = nsr[i]-nsl[i]-1
            area = height*base
            max_area = max(area, max_area)
        
        return max_area
