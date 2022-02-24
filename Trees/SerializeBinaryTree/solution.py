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
    def solve(self, A):
        queue = deque([A])
        result = []

        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                top = queue[0]
                if top:
                    result.append(top.val)
                    queue.append(top.left)
                    queue.append(top.right)
                else:
                    result.append(-1)
                queue.popleft()
        
        return result
