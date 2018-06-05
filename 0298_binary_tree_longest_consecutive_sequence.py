# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        else:
            return max(self.countSequence(root.left, root, 1), self.countSequence(root.right, root, 1))
    
    def countSequence(self, node, parent_node, count):
        if node is None:
            return count
        
        elif node.val == parent_node.val + 1:
            count = count + 1
            
            return max(count, self.countSequence(node.left, node, count), self.countSequence(node.right, node, count))
        
        else:
            return max(self.countSequence(node.left, node, 1), self.countSequence(node.right, node, 1))
