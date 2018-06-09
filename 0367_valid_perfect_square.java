class Solution {
    public boolean isPerfectSquare(int num) {
        int maxRoot = (int) Math.sqrt(Integer.MAX_VALUE); 
        
        for (int i = 1; i <= maxRoot; i++) {
            if (i * i == num) return true; 
            else if (i * i > num) break;  
        }
        
        return false; 
    }
}
