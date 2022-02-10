from collections import deque

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        queue = deque()
        result = ""
        hash_map = {}

        for i in range(len(A)):
            ele = A[i]
            if ele in hash_map.keys():
                hash_map[ele] += 1
            else:
                hash_map[ele] = 1
            
            queue.append(ele)
            while len(queue) > 0 and hash_map[queue[0]] > 1:
                queue.popleft()
            
            if len(queue) > 0:
                result = result + queue[0]
            else:
                result = result + "#"
        
        return result
