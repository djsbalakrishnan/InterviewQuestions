from heapq import heapify, heappush, heappop
import math

class Solution:
	# @param A : integer
	# @param B : list of integers
	# @return an integer
	def nchoc(self, A, B):
		heap = []
		heapify(heap)
		total = 0
		MOD = 1e9+7

		for ele in B:
			heappush(heap, -ele)
		
		for _ in range(A):
			max_ele = heappop(heap)
			total = (total + (-max_ele))%MOD
			max_ele = math.floor(-max_ele/2)
			heappush(heap, -max_ele)
		
		return int(total)
