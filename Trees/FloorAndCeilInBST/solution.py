# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        answers = []

        for ele in B:
            temp = A
            floor = -1
            ceil = -1

            while temp:
                if temp.val == ele:
                    floor = temp.val
                    ceil = temp.val
                    break
                elif temp.val < ele:
                    floor = temp.val
                    temp = temp.right
                else:
                    ceil = temp.val
                    temp = temp.left
            
            answers.append([floor, ceil])
        return answers
