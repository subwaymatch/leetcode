class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        tree_list = []
        
        self.traverse(root, tree_list)
        
        left_idx = 0
        right_idx = len(tree_list) - 1
        
        while left_idx < right_idx:
            sum = tree_list[left_idx] + tree_list[right_idx]
            
            if sum == k:
                return True
            
            elif sum < k:
                left_idx = left_idx + 1
            
            else:
                right_idx = right_idx - 1
        
        return False
        
    
    def traverse(self, node, tree_list):
        if node is None:
            return
        
        self.traverse(node.left, tree_list)
        tree_list.append(node.val)
        self.traverse(node.right, tree_list)
