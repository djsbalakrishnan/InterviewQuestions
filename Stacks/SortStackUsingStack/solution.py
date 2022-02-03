class Solution:
    def solve(self, A):
        duplicate = []
        while len(A) > 0:
            top_a = A[len(A) - 1]
            A.pop()
            while (len(duplicate) > 0) and (duplicate[len(duplicate) - 1] > top_a):
                A.append(duplicate[len(duplicate) - 1])
                duplicate.pop()
            duplicate.append(top_a)
        
        return duplicate
