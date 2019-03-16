class DeckSimulator:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add_card(self, val):
        new_node = self.Node(val)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        elif self.size == 1:
            self.head = new_node
            self.head.next = self.tail
            self.tail.prev = self.head
            
        else:
            prev_head = self.head
            
            self.head = new_node
            new_node.next = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            new_node.next.prev = new_node
            new_node.next.next = prev_head
            new_node.next.next.prev = new_node.next
            
        self.size += 1
        
    def to_list(self):
        l = []
        
        node = self.head
        
        while node is not None:
            l.append(node.val)
            node = node.next
            
        return l
        
    class Node:
        def __init__(self, val):
            self.prev = None
            self.next = None
            self.val = val

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ds = DeckSimulator()
        
        for num in reversed(sorted(deck)):
            ds.add_card(num)
        
        return ds.to_list()
