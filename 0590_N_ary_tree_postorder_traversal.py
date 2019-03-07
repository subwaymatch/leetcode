"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        order = []
        
        self.record_postorder(root, order)
        
        return order

    def record_postorder(self, root: 'Node', order: List[int]) -> None:
        if root is None:
            return
        
        for child in root.children:
            self.record_postorder(child, order)
        
        order.append(root.val)
