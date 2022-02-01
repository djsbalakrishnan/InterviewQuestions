# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # There are two approaches to solve this problem. I have used the easier way to solve this. 
    def solve(self, A):
        length = 0
        mid = 0
        index = 1
        temp = A
        
        # Find the length of the Linked List 
        while temp:
            length += 1
            temp = temp.next
        
        # Find the middle index for the given Linked List
        mid = (length//2) + 1

        # Iterate to get the middle value of Linked List
        temp = A
        while index < mid and temp:
            index += 1
            temp = temp.next
        
        return temp.val
