# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None:
            return None
        
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        
        if root.val < L:
            root = root.right
        elif root.val > R:
            root = root.left
            
        return root
