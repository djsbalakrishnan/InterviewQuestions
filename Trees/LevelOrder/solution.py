# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
from collections import deque

class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def levelOrder(self, A):
		queue = deque()
		queue.append(A)
		output = []

		while len(queue) > 0:
			size = len(queue)
			temp_output = []
			for i in range(size):
				top = queue[0]
				temp_output.append(top.val)
				if top.left:
					queue.append(top.left)
				if top.right:
					queue.append(top.right)
				queue.popleft()
				
			output.append(temp_output)
		
		return output
