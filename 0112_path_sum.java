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
    public boolean hasPathSum(TreeNode root, int sum) {
        return add(root, sum, 0); 
    }
    
    boolean add(TreeNode node, int sum, int currentSum) {
        if (node == null) return false; 
        else if ((node.left == null) && (node.right == null)) {
            if (sum == currentSum + node.val) return true; 
            else return false; 
        }
        else {
            return (add(node.left, sum, currentSum + node.val) || add(node.right, sum, currentSum + node.val)); 
        }
    }
}
