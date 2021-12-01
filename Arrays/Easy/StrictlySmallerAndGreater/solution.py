class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A) -> int:
        # find min and max O(n)
        # parse and count strictly between min and max
        min_val = min(A)
        max_val = max(A)
        result = 0
        
        for ele in A:
            if (ele > min_val) and (ele < max_val):
                result += 1
                
        return result
