from heapq import heapify, heappush, heappop

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        cost = 0
        heap = []
        heapify(heap)

        for ele in A:
            heappush(heap, ele)
        
        for i in range(len(A)-1):
            min_1 = heappop(heap)
            min_2 = heappop(heap)
            cost += min_1 + min_2
            heappush(heap, min_1 + min_2)
        
        return cost
