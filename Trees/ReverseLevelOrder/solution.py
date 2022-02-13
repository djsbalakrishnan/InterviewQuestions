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
        output = []
        size = len(queue)

        while len(queue) > 0:
            for index in range(size):
                top = queue[0]
                temp_output = [top.val]
                if top.right:
                    queue.append(top.right)
                if top.left:
                    queue.append(top.left)
                queue.popleft()
            
            output += temp_output

        return output[::-1]
