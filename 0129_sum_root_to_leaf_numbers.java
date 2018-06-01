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
    int sum = 0; 
    
    public int sumNumbers(TreeNode root) {
        if (root == null) return 0; 
        
        if (isLeaf(root)) {
            sum = root.val; 
        }
        
        else {
            search(root.left, root.val); 
            search(root.right, root.val); 
        }
        
        return sum; 
    }
    
    public void search(TreeNode node, int currentVal) {
        if (node == null) return; 
        
        currentVal = currentVal * 10 + node.val; 
        if (isLeaf(node) == true) sum += currentVal; 
        else {
            search(node.left, currentVal); 
            search(node.right, currentVal); 
        }
    }
    
    public boolean isLeaf(TreeNode node) {
        return (node.left == null && node.right == null);
    }
}
