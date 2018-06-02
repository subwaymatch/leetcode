# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level_order = []
        
        if root is None: 
            return level_order
        
        level_order.append([root.val])
        prev_level = [root]
        curr_level = []
        
        while len(prev_level) > 0:
            for node in prev_level:
                if node.left is not None:
                    curr_level.append(node.left)
                
                if node.right is not None:
                    curr_level.append(node.right)
                
            if len(curr_level) > 0:
                level = []
                for node in curr_level:
                    level.append(node.val)
                level_order.append(level)
            
            prev_level = curr_level
            curr_level = []
        
        return level_order
