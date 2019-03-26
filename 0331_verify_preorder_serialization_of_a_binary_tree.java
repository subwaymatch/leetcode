class Solution {
    public boolean isValidSerialization(String preorder) {
        if ("#".equals(preorder)) return true; 
        
        Stack nodeStack = new Stack(); 
        
        for (String node : preorder.split(",")) {
            if ("#".equals(node)) {
                if (nodeStack.isEmpty()) return false; 
                
                if ("#".equals(nodeStack.peek())) {
                    boolean shouldContinue = true; 
                    while (shouldContinue) {
                        nodeStack.pop(); 
                        
                        if (nodeStack.isEmpty()) return false; 
                        
                        String parentNode = (String) nodeStack.pop(); 
                        
                        if ("#".equals(parentNode)) return false; 
                        
                        if (nodeStack.isEmpty() || !"#".equals(nodeStack.peek())) {
                            shouldContinue = false; 
                            nodeStack.push("#"); 
                        }
                    }
                } else {
                    nodeStack.push(node); 
                }
            }

            else {
                nodeStack.push(node); 
            }
        }
        
        return (nodeStack.size() == 1) && ("#".equals(nodeStack.peek())); 
    }
}
