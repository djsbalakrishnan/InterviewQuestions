class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        prefix_sum_array = [0]
        running_sum = 0
        hash_check = {}
        for ele in A:
            running_sum += ele
            prefix_sum_array.append(running_sum)
        
        for ele in prefix_sum_array:
            if ele in hash_check.keys():
                return 1
            else:
                hash_check[ele] = 1
        
        return 0
