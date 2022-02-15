# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
    def height(self, root):
        if root is None:
            return 0
        
        left_height = self.height(root.left) + 1
        right_height = self.height(root.right) + 1
        return max(left_height, right_height)

	def isBalanced(self, A):
        if A is None:
            return 1
        
        left_height = self.height(A.left) + 1
        right_height = self.height(A.right) + 1
        
        if abs(left_height - right_height) <=1 and self.isBalanced(A.left) and self.isBalanced(A.right): 
            return 1
        
        return 0
