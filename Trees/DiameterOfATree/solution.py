# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def __init__(self):
        self.min_val = 1e9+7
        self.max_val = -1e9+7

    def height(self, root):
        if root is None:
            return 0
        
        return 1+ max(self.height(root.left), self.height(root.right))

    def solve(self, A):
        if A is None: 
            return 0
        
        left_height = self.height(A.left)
        right_height = self.height(A.right)

        left_diameter = self.solve(A.left)
        right_diameter = self.solve(A.right)

        return max(left_height + right_height, max(left_diameter, right_diameter))
