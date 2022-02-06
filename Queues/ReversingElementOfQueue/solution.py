from collections import deque

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        stack = []
        queue = deque(A)
        ans = deque()

        for i in range(B):
            top = queue.popleft()
            stack.append(top)
        
        while len(stack) > 0:
            p = stack.pop()
            ans.append(p)
        
        while len(queue) > 0:
            pl = queue.popleft()
            ans.append(pl)
        
        return ans
