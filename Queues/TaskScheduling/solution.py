
from collections import deque

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        scheduler_q = deque(A)
        clockcycle = 0

        for ele in B:
            t = scheduler_q.popleft()
            while t != ele:
                scheduler_q.append(t)
                t = scheduler_q.popleft()
                clockcycle += 1
            clockcycle += 1
        
        return clockcycle
