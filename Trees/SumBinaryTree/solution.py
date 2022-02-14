# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer

    def check_sum(self, root):
        if root is None:
            return 0

        return root.val + self.check_sum(root.left) + self.check_sum(root.right)

    def solve(self, A):
        if A is None:
            return 1
        
        if A.left is None and A.right is None:
            return 1
        
        ls = self.check_sum(A.left)
        rs = self.check_sum(A.right)
        
        if (A.val == ls + rs) and self.solve(A.left) and self.solve(A.right):
            return 1
        
        return 0
