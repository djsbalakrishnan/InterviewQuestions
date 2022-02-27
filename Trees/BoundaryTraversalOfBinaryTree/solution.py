# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def __init__(self):
        self.result = []
        self.left_nodes = []
        self.leaf_nodes = []
        self.right_nodes = []

    def inorder_traversal(self, root):
        if root is None: 
            return
        self.inorder_traversal(root.left)
        if root.left is None and root.right is None:
            self.leaf_nodes.append(root.val)
        self.inorder_traversal(root.right)
    
    def get_left_boundary(self, root):
        if root:
            if root.left:
                self.left_nodes.append(root.val)
                self.get_left_boundary(root.left)
            elif root.right:
                self.left_nodes.append(root.val)
                self.get_left_boundary(root.right)
    

    def get_right_boundary(self, root):
        if root:
            if root.right:
                self.get_right_boundary(root.right)
                self.right_nodes.append(root.val)
            elif root.left:
                self.get_right_boundary(root.right)
                self.right_nodes.append(root.val)    


    def solve(self, A):
        # left view
        self.get_left_boundary(A)
        # bottom view
        self.inorder_traversal(A)
        # right viewf
        self.get_right_boundary(A)
        
        return self.left_nodes + self.leaf_nodes + self.right_nodes[:-1]
