# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def createMid(self, A, left, right):
        if left > right:
            return None
        
        mid = (left + right)//2
        node = TreeNode(A[mid])
        node.left = self.createMid(A, left, mid - 1)
        node.right = self.createMid(A, mid+1, right)
        return node

    def sortedArrayToBST(self, A):
        node = self.createMid(A, 0, len(A)-1)
        return node
