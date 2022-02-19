# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @param C : integer
	# @return an integer
	def __init__(self):
		self.path_one = []
        self.path_two = []

    def findPath(self, root, val, path):
        if root is None: 
            return False

        path.append(root.val)
        if root.val == val:
            return True
        if ((root.left and self.findPath(root.left, val, path)) or (root.right and self.findPath(root.right, val, path))):
            return True
        
        path.pop()
        return False


	def lca(self, A, B, C):
        if self.findPath(A, B, self.path_one) and self.findPath(A, C, self.path_two):
            i = 0
            while i < len(self.path_one) and i < len(self.path_two):
                if self.path_one[i] != self.path_two[i]:
                    break
                i += 1
            return self.path_one[i-1]    

        return -1
