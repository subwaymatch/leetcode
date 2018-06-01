# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            node = None
            
        elif t1 is None: 
            node = t2
            
        elif t2 is None:
            node = t1
            
        else:
            node = TreeNode(t1.val + t2.val)
        
        if node is not None:
            if t1 is not None and t2 is not None:
                node.left = self.mergeTrees(t1.left, t2.left)
                node.right = self.mergeTrees(t1.right, t2.right)
                
            elif t1 is None: 
                node.left = self.mergeTrees(None, t2.left)
                node.right = self.mergeTrees(None, t2.right)

            elif t2 is None:
                node.left = self.mergeTrees(t1.left, None)
                node.right = self.mergeTrees(t1.right, None)
            
        return node
