# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
from collections import deque

class Solution:
	# @param A : root node of tree
	# @return the root node in the tree
    def invert(self, A):
        if A is None:
            return 
        else:
            A.left, A.right = A.right, A.left
            self.invert(A.left)
            self.invert(A.right)
            return

	def invertTree(self, A):
        head = A
        self.invert(head)
        return A
