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
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> paths = new ArrayList<List<Integer>>(); 
        List<Integer> path = new ArrayList<Integer>(); 
        
        add(root, paths, path, sum, 0);
        
        return paths; 
    }
    
    void add(TreeNode node, List<List<Integer>> paths, List<Integer> path, int target, int sumSoFar) {
        if (node == null) return; 
        
        sumSoFar += node.val; 
        path.add(node.val); 
        
        if (node.left == null && node.right == null) {
            if (sumSoFar == target) paths.add(new ArrayList<Integer>(path)); 
        }
    
        else {
            add(node.left, paths, path, target, sumSoFar); 
            add(node.right, paths, path, target, sumSoFar); 
        }
        
        sumSoFar -= node.val; 
        path.remove(path.size() - 1); 
    }
}
