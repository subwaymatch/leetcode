# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getNodeVal(self, node):
        if node == None:
            return None
        else:
            return node.val
        
    def swapChildren(self, node):
        tempNode = node.left
        node.left = node.right
        node.right = tempNode
        
    def isFlipEquivalent(self, node1: TreeNode, node2: TreeNode):
        if self.getNodeVal(node1) != self.getNodeVal(node2):
            return False
        
        if node1 == None and node2 == None:
            return True
        
        elif node1 == None or node2 == None:
            return False
        
        if self.getNodeVal(node1.left) != self.getNodeVal(node2.left):
            self.swapChildren(node1)
        
        return self.isFlipEquivalent(node1.left, node2.left) and self.isFlipEquivalent(node1.right, node2.right)
    
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.isFlipEquivalent(root1, root2)
        
