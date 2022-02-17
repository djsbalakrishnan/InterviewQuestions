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
    def __init__(self):
        self.inorder = []

    def inorderTraversal(self, root):
        if root is None:
            return None
        
        self.inorderTraversal(root.left)
        self.inorder.append(root.val)
        self.inorderTraversal(root.right)

	def kthsmallest(self, A, B):
        self.inorderTraversal(A)
        return self.inorder[B-1]
