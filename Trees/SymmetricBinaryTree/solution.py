# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

from collections import deque

class Solution:
	# @param A : root node of tree
	# @return an integer
    def isMirrorImage(self, A, B):
        if A is None and B is None: 
            return 1
        
        if A and B and A.val == B.val:
            return self.isMirrorImage(A.left, B.right) and self.isMirrorImage(A.right, B.left)
        
        return 0

	def isSymmetric(self, A):
        return self.isMirrorImage(A, A)
