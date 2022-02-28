class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        for index in range(len(A)):
            if A[index] == 0:
                A[index] = -1
        
        prefix_sum_arr = [0]
        sum = 0
        for index in range(len(A)):
            sum += A[index]
            prefix_sum_arr.append(sum)
        
        hash_a = {}
        max_len_sub_arr = 0
        for index in range(len(prefix_sum_arr)):
            if prefix_sum_arr[index] in hash_a.keys():
                hash_a[prefix_sum_arr[index]][1] = index
                index_diff = index - hash_a[prefix_sum_arr[index]][0]
                if index_diff > max_len_sub_arr:
                    max_len_sub_arr = index_diff
            else:
                hash_a[prefix_sum_arr[index]] = [index, index]
        
        return max_len_sub_arr
