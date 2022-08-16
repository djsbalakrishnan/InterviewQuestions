class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def solve(self, A, B):
        answer = []
        p1, p2 = 0, 0
        while p1 < len(A) and p2< len(B):
            if A[p1] <= B[p2]:
                answer.append(A[p1])
                p1 += 1
            else:
                answer.append(B[p2])
                p2 += 1
        
        if p1 == len(A):
            answer += B[p2:]
        if p2 == len(B):
            answer += A[p1:]
        
        return answer
