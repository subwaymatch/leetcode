/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    private int minDiff = Integer.MAX_VALUE;
    public int getMinimumDifference(TreeNode root) {
        inOrder(root, null);
        
        return minDiff;
    }
    
    public TreeNode inOrder(TreeNode node, TreeNode prevNode) {
        if (node == null) return prevNode; 
        prevNode = inOrder(node.left, prevNode); 
        
        if (prevNode != null) {
            minDiff = Math.min(minDiff, Math.abs(prevNode.val - node.val));
        }
        
        return inOrder(node.right, node); 
    }
}
