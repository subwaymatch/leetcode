# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        level_sum = 0
        
        averages = []
        curr_level = [root]
        next_level = []
        level_count = 0
        
        while curr_level:
            node = curr_level.pop()
            
            if node is not None:
                level_sum += node.val
                level_count += 1

                next_level.append(node.left)
                next_level.append(node.right)
            
            if not curr_level and level_count > 0:
                averages.append(level_sum / level_count)
                curr_level = next_level
                next_level = []
                level_sum = 0
                level_count = 0
        
        return averages
