/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class CBTInserter {
    private TreeNode root;
    private Queue<TreeNode> parentQueue; 
    private Queue<TreeNode> currQueue; 
    
    public CBTInserter(TreeNode root) {
        // Construct the tree and pareentQueue; 
        this.root = root; 
        
        this.parentQueue = new LinkedList<>(); 
        this.currQueue = new LinkedList<>();
        
        parentQueue.add(root); 
        
        while (!parentQueue.isEmpty()) {
            TreeNode node = parentQueue.peek(); 
            
            if (node.left != null) currQueue.add(node.left); 
            if (node.right != null) currQueue.add(node.right); 
            
            if (node.left != null && node.right != null) {
                parentQueue.remove(); 
            } else {
                break; 
            }
            
            if (parentQueue.isEmpty()) {
                parentQueue = currQueue; 
                currQueue = new LinkedList<>(); 
            }
        }
    }
    
    public int insert(int v) {
        TreeNode newNode = new TreeNode(v); 
        TreeNode parentNode = parentQueue.peek(); 
        
        if (parentNode.left == null) parentNode.left = newNode; 
        else {
            parentNode.right = newNode; 
            parentQueue.remove(); 
        }
        
        currQueue.add(newNode); 
        
        if (parentQueue.isEmpty()) {
            parentQueue = currQueue; 
            currQueue = new LinkedList<>(); 
        }
        
        return parentNode.val; 
    }
    
    public TreeNode get_root() {
        return this.root; 
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj = new CBTInserter(root);
 * int param_1 = obj.insert(v);
 * TreeNode param_2 = obj.get_root();
 */
