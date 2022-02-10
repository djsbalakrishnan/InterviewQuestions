class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLongestSubstring(self, A):
        last_index_map = {}
        start_index = 0
        longest_substring = 0
        for index in range(len(A)):
            ele = A[index]
            if ele in last_index_map.keys():
                # Update the Start Index 
                start_index = max(start_index, last_index_map[ele]+1)
                last_index_map[ele] = index
            else:
                last_index_map[ele] = index
            length_of_substring = index - start_index + 1
            longest_substring = max(length_of_substring, longest_substring)
        
        return longest_substring
