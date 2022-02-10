# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
    def __init__(self):
        self.result = []
    
	def inorderTraversal(self, A):
        if A is None:
            return 
        self.inorderTraversal(A.left)
        self.result.append(A.val)
        self.inorderTraversal(A.right)
        
        return self.result

