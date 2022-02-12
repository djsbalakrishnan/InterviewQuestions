class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        hash_x = {}
        hash_y = {}
        count = 0
        MOD = 1e9+7

        for i in range(len(A)):
            x = A[i]
            y = B[i]

            if x in hash_x.keys():
                hash_x[x] += 1
            else:
                hash_x[x] = 1
            if y in hash_y.keys():
                hash_y[y] += 1
            else:
                hash_y[y] = 1
        
        for i in range(len(A)):
            x = hash_x[A[i]]
            y = hash_y[B[i]]

            if x>=1 and y>=1:
                count = (count%MOD + (((x-1)*(y-1))%MOD))%MOD
        
        return int(count)
