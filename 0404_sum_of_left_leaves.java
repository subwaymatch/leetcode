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
    public int traverse(TreeNode root, boolean isLeft) {
        if (root == null) return 0; 
        
        else if (isLeft && root.left == null && root.right == null) return root.val; 
        else return traverse(root.left, true) + traverse(root.right, false); 
        
    }
    
    public int sumOfLeftLeaves(TreeNode root) {
        if (root == null) return 0; 
        
        return traverse(root.left, true) + traverse(root.right, false); 
    }
}
