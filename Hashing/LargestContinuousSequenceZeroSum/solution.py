class Solution:
	# @param A : list of integers
	# @return a list of integers
	def lszero(self, A):
        prefix_sum_arr = [0]
        hash_prefix_sum_A = {}
        running_sum = 0
        longest_seq = 0
        result = []
        
        for ele in A:
            running_sum += ele
            prefix_sum_arr.append(running_sum)
        
        for i in range(len(prefix_sum_arr)):
            ele = prefix_sum_arr[i]
            if ele in hash_prefix_sum_A.keys():
                difference = i - hash_prefix_sum_A[ele]
                if difference > longest_seq:
                    longest_seq = difference
                    result = A[hash_prefix_sum_A[ele]: i]
            else:
                hash_prefix_sum_A[ele] = i
        
        return result
