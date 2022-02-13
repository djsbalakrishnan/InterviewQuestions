# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
from collections import deque

class Solution:
	# @param A : root node of tree
	# @return a list of list of integers

	def verticalOrderTraversal(self, A):
        hash_level_to_node = {}
        hash_node_to_level = {A:0}
        queue = deque([A])
        min_val, max_val = 1e9, -1e9

        while len(queue) > 0:
            size = len(queue)

            for i in range(size):
                top = queue[0]
                node_level = hash_node_to_level[top]

                min_val = min(node_level, min_val)
                max_val = max(node_level, max_val)

                if node_level in hash_level_to_node.keys():
                    hash_level_to_node[node_level].append(top.val)
                else:
                    hash_level_to_node[node_level] = [top.val]
                
                if top.left:
                    hash_node_to_level[top.left] = node_level - 1
                    queue.append(top.left)
                if top.right:
                    hash_node_to_level[top.right] = node_level + 1
                    queue.append(top.right)
                
                queue.popleft()
                
        output = []
        for v_level in range(min_val, max_val + 1):
            if v_level in hash_level_to_node.keys():
                output.append(hash_level_to_node[v_level])
            
        return output
