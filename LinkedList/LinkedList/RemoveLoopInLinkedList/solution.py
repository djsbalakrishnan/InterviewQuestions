# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        p1, p2 = None, A
        hash_a = {}
        
        while p2:
            if p2 in hash_a.keys():
                p1.next = None
                return A
            else:
                hash_a[p2] = True
                p1 = p2
                p2 = p2.next
