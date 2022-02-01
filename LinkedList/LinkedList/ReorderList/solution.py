# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def reverse(self, node):
        prev = None
        curr = node
        nex = None
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        return prev

    def reorderList(self, A):
        # find middle 
        # reverse the elements after middle element 
        # alternatively arrange the elements in first ll and reversed ll
        slow, fast = A, A

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        mid_next = slow.next
        mid.next = None

        mid_reverse = self.reverse(mid_next)
        start = A

        node = ListNode(0)
        new_node = node
        
        while mid_reverse or start:
            if start:
                new_node.next = start
                new_node = new_node.next
                start = start.next

            if mid_reverse:
                new_node.next = mid_reverse
                new_node = new_node.next
                mid_reverse = mid_reverse.next
        
        node = node.next
        return node 

