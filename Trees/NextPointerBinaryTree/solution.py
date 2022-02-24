# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        queue = deque()
        queue.append(root)
        root.next = None
        prev = None
        while len(queue) > 0:
            size = len(queue)
			for i in range(size):
                top = queue[0]
                if prev:
                    prev.next = top
                prev = top
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
                queue.popleft()
            prev = None
        
        return root
