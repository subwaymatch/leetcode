# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        largest_list = []
        
        self.search(root, 0, largest_list)
        
        return largest_list
        
    
    def search(self, node, depth, largest_list):
        if node is None:
            return
        
        if len(largest_list) < depth + 1:
            largest_list.append(node.val)
            
        elif largest_list[depth] < node.val:
            largest_list[depth] = node.val
        
        self.search(node.left, depth + 1, largest_list)
        self.search(node.right, depth + 1, largest_list)
