# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def __init__(self):
        self.result = 0

    def modified_inorder(self, A, B, C):
        if A is None:
            return
        
        if A.val >= B and A.val <= C:
            self.result += 1
        if A.val > C:
            # need not traverse to right
            self.modified_inorder(A.left, B, C)
        elif A.val < B:
            # need not traverse to left
            self.modified_inorder(A.right, B, C)
        else:
            self.modified_inorder(A.left, B, C)
            self.modified_inorder(A.right, B, C)

    def solve(self, A, B, C):
        self.modified_inorder(A, B, C)
        return self.result
