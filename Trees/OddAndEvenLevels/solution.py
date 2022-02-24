# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        queue = deque()
        queue.append(A)
        even_sum = 0
        odd_sum = 0
        level = 1
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                top = queue[0]
                if level%2 == 1:
                    odd_sum += top.val
                else:
                    even_sum += top.val
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
                queue.popleft()
            
            level += 1

        return odd_sum - even_sum
