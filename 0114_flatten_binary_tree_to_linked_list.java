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
    public void flatten(TreeNode root) {
        flattenHelper(root);
    }
    
    // Returns the last node of the flattened list
    public TreeNode flattenHelper(TreeNode node) {
        if (node == null) {
            return null;
        }

        if ((node.left == null) && (node.right == null)) {
            return node;
        }

        if ((node.left != null) && (node.right != null)) {
            TreeNode originalRightNode = node.right;

            TreeNode leftTailNode = flattenHelper(node.left); 
            TreeNode rightTailNode = flattenHelper(node.right);

            node.right = node.left; 
            node.left = null;

            leftTailNode.right = originalRightNode;

            return rightTailNode; 
        }

        else if (node.left == null) {
            return flattenHelper(node.right);
        }

        else {
            node.right = node.left; 
            node.left = null; 

            return flattenHelper(node.right);
        }
    }
}
