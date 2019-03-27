class Solution {
    public boolean isCompleteTree(TreeNode root) {
        Queue<TreeNode> currLevel = new LinkedList<>(); 
        Queue<TreeNode> nextLevel = new LinkedList<>(); 
        int expectedNumChildNodes = 2;
        boolean isLastRow = false; 

        currLevel.add(root); 

        while (!currLevel.isEmpty()) {
            TreeNode node = currLevel.poll(); 
            
            if (node.left == null) isLastRow = true; 
            else if (isLastRow) return false; 
            else nextLevel.add(node.left);

            if (node.right == null) isLastRow = true; 
            else if (isLastRow) return false; 
            else nextLevel.add(node.right); 

            if (currLevel.isEmpty()) {
                if (isLastRow) break; 
                else if (nextLevel.size() != expectedNumChildNodes)  {
                    return false; 
                }
                else {
                    currLevel = nextLevel; 
                    nextLevel = new LinkedList<>();
                    expectedNumChildNodes *= 2;
                }
            }
        }

        while (!nextLevel.isEmpty()) {
            TreeNode node = nextLevel.poll();

            if (node.left != null || node.right != null) return false; 
        }

        return true;   
    }
}
