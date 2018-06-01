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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> traversalList = new ArrayList<Integer>(); 
        
        traverse(traversalList, root); 
        
        return traversalList; 
    }
    
    void traverse(List<Integer> traversalList, TreeNode node) {
        if (node == null) return;
        
        traverse(traversalList, node.left); 
        traversalList.add(node.val); 
        traverse(traversalList, node.right);         
    }
    
    
}
