# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
    def pathSum(self, root, B, sum_val):
        if root is None:
            return 0

        sum_val += root.val
        if root.left == None and root.right == None:
            if sum_val == B:
                return 1    
        return self.pathSum(root.left, B, sum_val) or self.pathSum(root.right, B, sum_val)
	
    
    def hasPathSum(self, A, B):
        return self.pathSum(A, B, 0)
