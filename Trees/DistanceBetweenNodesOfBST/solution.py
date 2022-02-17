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

    def find_distance_from_parent(self, root, val):
        if root.val == val:
            return 0
        
        if root.val > val:
            return self.find_distance_from_parent(root.left, val) + 1
        else:
            return self.find_distance_from_parent(root.right, val) + 1


    def find_distance(self, root, val1, val2):
        if root is None: 
            return 0
        if root.val > val1 and root.val > val2:
            return self.find_distance(root.left, val1, val2)
        
        elif root.val < val1 and root.val < val2:
            return self.find_distance(root.right, val1, val2)
        else:
            return self.find_distance_from_parent(root, val1) + self.find_distance_from_parent(root, val2)


    def solve(self, A, B, C):
        distance = self.find_distance(A, B, C)
        return distance
