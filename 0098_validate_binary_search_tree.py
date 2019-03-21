# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid_BST(root)[0]
    
    # Return is_valid, min, max
    def is_valid_BST(self, node: TreeNode) -> (bool, int, int):
        if node is None:
            return (True, None, None)
        
        is_left_valid, left_min, left_max = self.is_valid_BST(node.left)
        is_right_valid, right_min, right_max = self.is_valid_BST(node.right)
        
        if not is_left_valid or not is_right_valid:
            return (False, None, None)
        
        if (left_max is not None and node.val <= left_max) or (right_min is not None and node.val >= right_min):
            return (False, None, None)
        
        else:
            return (True, node.val if left_min is None else left_min, node.val if right_max is None else right_max)
