# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    backtrack = None
    current_node = None

    def __init__(self, root: TreeNode):
        root_pointer = TreeNode(-1, None, root)
        
        self.backtrack = [root_pointer]
        self.current_node = root_pointer

    def next(self) -> int:
        """
        @return the next smallest number
        """      
        if self.backtrack[-1] == self.current_node:
            last_node = self.backtrack.pop()
            
            return self.next() if last_node.right is None else self.traverse(last_node.right)
        else:
            last_node = self.backtrack[-1]
            self.current_node = last_node
            return self.current_node.val

    def hasNext(self) -> bool:
        if len(self.backtrack) > 1:
            return True
        elif len(self.backtrack) == 1:
            if self.backtrack[-1] == self.current_node:
                return self.backtrack[-1].right is not None
            else:
                return True
    
    def traverse(self, node) -> int:
        if node.left:
            self.backtrack.append(node)
            return self.traverse(node.left)
        
        if node.right:
            self.backtrack.append(node)
        
        self.current_node = node
        return node.val
    

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
