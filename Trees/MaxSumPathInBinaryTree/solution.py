# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
    def __init__(self):
        self.max_val = -1e9
    
    
    def maxPathSumUtil(self, root):
        if root is None:
            return 0
        
        left = self.maxPathSumUtil(root.left)
        right = self.maxPathSumUtil(root.right)
        max_single_side = max(max(left, right) + root.val, root.val)
        max_top = max(max_single_side, left + right + root.val)
        self.max_val = max(self.max_val, max_top)
        
        return max_single_side

	def maxPathSum(self, A):
        self.maxPathSumUtil(A)
        return self.max_val
