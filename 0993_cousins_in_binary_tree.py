# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None or root == x or root == y:
            return False
        
        first_parent = None
        
        curr_level = [(root, None)]
        next_level = []
        
        while curr_level:
            node, parent = curr_level.pop(0)
            
            if node is not None:
                if node.val == x or node.val == y:
                    if first_parent is None:
                        first_parent = parent
                        
                    else:
                        return parent != first_parent
                
                next_level.append((node.left, node))
                next_level.append((node.right, node))
                
            if not curr_level:
                if first_parent:
                    return False
                
                curr_level = next_level
                next_level = []
                
        return False
