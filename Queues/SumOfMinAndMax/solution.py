from collections import deque

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        max_queue = deque()
        min_queue = deque()
        result = 0
        MOD = 1e9 + 7
        for i in range(B):    
            val = A[i]
            while len(max_queue) > 0 and val > max_queue[-1]:
                max_queue.pop()
            while len(min_queue) > 0 and val < min_queue[-1]:
                min_queue.pop()
            min_queue.append(val)
            max_queue.append(val)
            
        result = ((result%MOD)+ (max_queue[0]%MOD) + (min_queue[0]%MOD))%MOD
        result = (result+MOD)%MOD
        for i in range(B, len(A)):
            start_val = A[i-B]
            end_val = A[i]
            if max_queue[0] == start_val:
                max_queue.popleft()
            if min_queue[0] == start_val:
                min_queue.popleft()
            while len(max_queue) > 0 and end_val > max_queue[-1]:
                max_queue.pop()
            while len(min_queue) > 0 and end_val < min_queue[-1]:
                min_queue.pop()
            min_queue.append(end_val)
            max_queue.append(end_val)
            result = ((result%MOD)+ (max_queue[0]%MOD) + (min_queue[0]%MOD))%MOD
        
        return int((result+MOD)%MOD)
