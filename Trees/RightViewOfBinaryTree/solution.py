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
        output, result = [], []

        while len(queue) > 0:
            size = len(queue)
            temp_output = []
            for i in range(size):
                top = queue[0]
                temp_output.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
                queue.popleft()    
            output.append(temp_output)
        
        for a in output:
            result.append(a[-1])
            
        return result
