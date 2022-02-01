# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:

    def reverseList(self, A, B):
        # If head is None return as is (base case)
        if A == None:
            return None
        p, n = None, None
        curr = A
        count = 0

        while curr and count < B:
            n = curr.next
            curr.next = p
            p = curr
            curr = n
            count += 1

        if n is not None:
            A.next = self.reverseList(n, B)
        
        return p