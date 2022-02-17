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
		self.first = None
		self.second = None
		self.prev = None

	def inorderTraversal(self, root):
		if root is None: 
			return None
		
		self.inorderTraversal(root.left)
		if self.prev and self.prev.val > root.val:
			if self.first is None:
				self.first = self.prev
			self.second = root
		self.prev = root
		self.inorderTraversal(root.right)

	def recoverTree(self, A):
		self.inorderTraversal(A)
        return [self.first.val, self.second.val]
