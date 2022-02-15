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
        self.inorder = []

    def inorderTraversal(self, A):
        if A is None:
            return
        
        self.inorderTraversal(A.left)
        self.inorder.append(A.val)
        self.inorderTraversal(A.right)

	def isValidBST(self, A):
        self.inorderTraversal(A)
        for i in range(len(self.inorder)-1):
            if self.inorder[i+1] <= self.inorder[i]:
                return 0
        
        return 1
