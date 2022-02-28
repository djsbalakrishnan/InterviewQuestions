class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        A.sort()
        res = []
        hash_a = {}
        for ele in A:
            if ele in hash_a.keys():
                hash_a[ele] += 1
            else:
                hash_a[ele] = 1
        
        for ele in B:
            if ele in hash_a.keys():
                res += [ele]*hash_a[ele]
                hash_a[ele] = 0
        
        for ele in A:
            if hash_a[ele] != 0:
                res += [ele]
        
        return res
