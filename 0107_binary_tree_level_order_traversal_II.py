class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        traverseList = []
        
        self.traverse([root], traverseList)
        
        return list(reversed(traverseList))
        
    def traverse(self, nodes: List[TreeNode], traverseList: List[List[int]]):
        newNodes = []
        nodeValues = []
        
        for node in nodes:
            if node == None:
                continue
            
            newNodes.append(node.left)
            newNodes.append(node.right)
            
            nodeValues.append(node.val)
        
        if nodeValues:
            traverseList.append(nodeValues)
        
        if newNodes:
            self.traverse(newNodes, traverseList)
