# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.build_tree(nums, 0, len(nums) - 1)
        
    
    def build_tree(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None
        
        elif left == right:
            return TreeNode(nums[left])
        
        else:
            mid = left + int((right - left + 1) / 2)
            
            new_node = TreeNode(nums[mid])
            
            new_node.left = self.build_tree(nums, left, mid - 1)
            new_node.right = self.build_tree(nums, mid + 1, right)
            
            return new_node
