from heapq import heapify, heappush, heappop, nsmallest

class Solution:
    def solve(self, A):
        min_heap = [] # right elements
        max_heap = [] # left elements
        heapify(min_heap)
        heapify(max_heap)
        result = []
        median = -1

        for ele in A:
            if ele > median:
                heappush(min_heap, ele)
            else:
                heappush(max_heap, -ele)
            
            if len(min_heap) - len(max_heap) == 1:
                median = min_heap[0]
            elif len(max_heap) - len(min_heap) == 1:
                median = max_heap[0]*-1
            elif len(max_heap) - len(min_heap) == 0:
                median = max_heap[0]*-1
            else:
                if len(max_heap) - len(min_heap) == 2:
                    max_pop = (heappop(max_heap))*-1
                    heappush(min_heap, max_pop)
                elif len(min_heap) - len(max_heap) == 2:
                    min_pop = heappop(min_heap)
                    heappush(max_heap, -min_pop)
                median = max_heap[0]*-1
            result.append(median)
        
        return result
