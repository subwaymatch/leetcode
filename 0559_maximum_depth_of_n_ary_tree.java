class Solution {
    public int maxDepth(Node root) {
        if (root == null)
            return 0;
            
        else {
            int currMaxDepth = 0;
            int childMaxDepth = 0;
            
            for (Node child : root.children) {
                childMaxDepth = maxDepth(child);
                
                currMaxDepth = (currMaxDepth > childMaxDepth) ? currMaxDepth : childMaxDepth;
            }
            
            return currMaxDepth + 1;
        }
    }
}
