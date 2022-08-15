class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
	    A = sorted(A)
	    return A[B-1]
