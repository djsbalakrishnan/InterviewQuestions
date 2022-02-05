class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.hash_queue = {}


    def check_capacity_and_update(self):
        if len(self.hash_queue) > self.capacity:
            head_key = self.head.key
            self.head = self.head.next
            self.head.prev = None
            del self.hash_queue[head_key]


    def update_tail(self, addr):
        if self.tail is not None:
            self.tail.next = addr
            addr.prev = self.tail
            addr.next = None
            self.tail = addr
        else:
            self.head = addr
            self.tail = addr
        
        self.hash_queue[addr.key] = addr


    def remove_node(self, addr):
        prev_node = addr.prev
        next_node = addr.next
        # The addr can be both head and tail node 
        if len(self.hash_queue) == 1:
            self.head = None
            self.tail = None
        # The addr can be head node
        elif prev_node == None:
            self.head = self.head.next
            self.head.prev = None
        # The addr can be tail node
        elif next_node == None:
            self.tail = self.tail.prev
            self.tail.next = None
        # There could be only one node 
        else:
            prev_node.next = next_node
            next_node.prev = prev_node
        
        del self.hash_queue[addr.key]


    
    def get(self, key):
        # Check if key is available in hash_queue
        if key in self.hash_queue.keys():
            addr = self.hash_queue[key]
            self.remove_node(addr)
            self.update_tail(addr)
            return addr.val
        else:
            return -1

    
    def set(self, key, value):
        # check if key is available in hash_queue
        if key in self.hash_queue.keys():
            addr = self.hash_queue[key]
            addr.val = value
            self.remove_node(addr)
            self.update_tail(addr)
            self.check_capacity_and_update()
        else:
            addr = ListNode(key, value)
            self.hash_queue[key] = addr
            self.update_tail(addr)
            self.check_capacity_and_update()
