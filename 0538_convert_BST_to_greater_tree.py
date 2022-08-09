# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    running_sum = 0
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root
        
    def traverse(self, node: Optional[TreeNode]):
        if node is None:
            return
        
        self.traverse(node.right)
        self.running_sum += node.val
        node.val = self.running_sum
        self.traverse(node.left)
