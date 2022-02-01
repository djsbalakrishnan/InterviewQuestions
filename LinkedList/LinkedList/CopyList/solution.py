# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def display(self, node):
        n = node
        while n:
            print(n.value)
            n = n.next


    def copyRandomList(self, head):
        temp = head
        head_copy = None
        temp_copy = None
        hash_ad_map_ca = {}
        hash_ad_map_ac = {}
        while temp:
            temp_created = RandomListNode(temp.label)
            if head_copy is None:
                head_copy = temp_created
                temp_copy = temp_created
            else:
                temp_copy.next = temp_created
                temp_copy = temp_created
            hash_ad_map_ca[temp_copy] = temp
            hash_ad_map_ac[temp] = temp_copy
            temp = temp.next
        
        temp_copy = head_copy
        while temp_copy:
            node_actual = hash_ad_map_ca[temp_copy]
            random_from_actual = node_actual.random
            if random_from_actual:
                corresponding_rn = hash_ad_map_ac[random_from_actual]
                temp_copy.random = corresponding_rn
            temp_copy = temp_copy.next

        return head_copy
