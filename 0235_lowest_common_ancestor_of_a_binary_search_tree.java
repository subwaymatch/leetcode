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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode largerNode = (p.val > q.val) ? p : q; 
        TreeNode smallerNode = (largerNode == p) ? q : p;
        
        if (root.val == smallerNode.val || root.val == largerNode.val || (smallerNode.val < root.val && largerNode.val > root.val)) return root; 
        
        else if (smallerNode.val > root.val) return lowestCommonAncestor(root.right, p, q); 
        else return lowestCommonAncestor(root.left, p, q); 
    }
}
