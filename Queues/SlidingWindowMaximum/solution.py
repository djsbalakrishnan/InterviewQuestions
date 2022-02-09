from collections import deque
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def slidingMaximum(self, A, B):
        result = []
        queue = deque()
        
        for i in range(B):    
            val = A[i]
            while len(queue) > 0 and val > queue[-1]:
                queue.pop()
            queue.append(val)
        
        result.append(queue[0])
        for i in range(B, len(A)):
            start_val = A[i-B]
            end_val = A[i]
            if queue[0] == start_val:
                queue.popleft()
            while len(queue) > 0 and end_val > queue[-1]:
                queue.pop()
            queue.append(end_val)
            result.append(queue[0])
        
        return result
