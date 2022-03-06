from heapq import heapify, heappush, heappop

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        heap = []
        heapify(heap)
        ans = -1

        for i in range(len(A)):
            for j in range(len(A[i])):
                heappush(heap, A[i][j])
        
        for _ in range(B):
            ans = heappop(heap)
        
        return ans
