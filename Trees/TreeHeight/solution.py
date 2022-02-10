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
    def __init__(self):
        self.height = 0
    
    def solve(self, A):
        if A is None:
            return 0
        else:
            return max(self.solve(A.left), self.solve(A.right)) + 1
