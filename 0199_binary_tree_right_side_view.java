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
    int currentSearchedDepth; 
    public List<Integer> rightIndices = new ArrayList<Integer>();
    public List<Integer> rightValues = new ArrayList<Integer>(); 
    
    public List<Integer> rightSideView(TreeNode root) {
        currentSearchedDepth = -1; 
        
        traverse(root, 0, 1);
        
        return rightValues; 
    }
    
    public void traverse(TreeNode node, int depth, int hIndex) {
        if (node == null) return; 
        
        if (depth > currentSearchedDepth) {
            rightIndices.add(hIndex); 
            rightValues.add(node.val); 
            
            currentSearchedDepth = depth; 
        }
        
        else {
            if (hIndex > rightIndices.get(depth)) {
                rightIndices.set(depth, hIndex); 
                rightValues.set(depth, node.val); 
            }
        }
        
        traverse(node.left, depth + 1, hIndex * 2 - 1); 
        traverse(node.right, depth + 1, hIndex * 2 + 1);
    }
}
