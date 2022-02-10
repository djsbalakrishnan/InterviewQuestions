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

    
	def postorderTraversal(self, A):
        if A is None:
            return
        self.postorderTraversal(A.left)
        self.postorderTraversal(A.right)
        self.result.append(A.val)

        return self.result
