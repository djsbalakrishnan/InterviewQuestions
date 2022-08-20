class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A = sorted(A)
        min_diff = 1e9+7
        for index in range(len(A)-1):
            diff = A[index+1] - A[index]
            min_diff = min(min_diff, diff)
        
        return min_diff
