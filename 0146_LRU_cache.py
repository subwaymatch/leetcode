class LinkedListQueue:
    def __init__(self):
        self.node_lookup_map = {}
        self.head = None
        self.tail = None
    
    # Put a new key, or mark an existing key as used
    def queue(self, val: int) -> None:
        #print('queue(val=%d)' %(val))
        # In case an existing key is "used"
        if val in self.node_lookup_map:
            # If the used key is the only key in Q,
            # or if the used key is already the most recently used one, 
            # do nothing
            if len(self.node_lookup_map) == 1 or self.node_lookup_map[val] == self.head:
                return
            
            # Lookup the key and retrieve the ListNode object
            used_node = self.node_lookup_map[val]
        
            # If a previous node exists, link it to the next node
            if used_node.prev is not None:
                used_node.prev.next = used_node.next
                
                # If used node is a tail, make the previous node as the new tail
                if used_node == self.tail:
                    self.tail = used_node.prev
                    
            # If a next node exists, link its prev to the previous node
            if used_node.next is not None:
                used_node.next.prev = used_node.prev
                
            # Make current node the head
            used_node.next = self.head
            self.head.prev = used_node
            used_node.prev = None
            self.head = used_node
        
        # In case a new node is added
        else:
            new_node = self.ListNode(val)
            
            # Add the new ListNode to lookup dict
            self.node_lookup_map[val] = new_node

            if self.head is None:
                self.head = new_node
                self.tail = new_node
            
            else:
                # Make it as a new head
                self.head.prev = new_node
                new_node.next = self.head
                self.head = new_node
    
    # Get least recently used key
    def dequeue(self) -> int:
        dequeued_node = self.tail
        
        if len(self.node_lookup_map) == 1:
            self.head = None
            self.tail = None
        
        else:
            dequeued_node.prev.next = None
            self.tail = dequeued_node.prev
        
        self.node_lookup_map.pop(dequeued_node.val)
        
        return dequeued_node.val
    
    class ListNode:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None
    
    
class LRUCache:
    def __init__(self, capacity: int):
        self.cache_map = {}
        self.capacity = capacity
        self.q = LinkedListQueue()

    def get(self, key: int) -> int:
        if key in self.cache_map:
            self.q.queue(key)
            return self.cache_map[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map or len(self.cache_map) < self.capacity:
            self.cache_map[key] = value
            self.q.queue(key)
            
        else:
            lru_key = self.q.dequeue()
            self.cache_map.pop(lru_key)
            self.q.queue(key)
            self.cache_map[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
