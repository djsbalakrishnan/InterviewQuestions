# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys

sys. setrecursionlimit(1000000)

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        if A is None:
            return 0
        # This is as simple as counting the current node and calling for left and right node.
        return 1 + self.solve(A.left) + self.solve(A.right)

