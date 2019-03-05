class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n <= 0) return false; 
        
        int oneBitCount = 0; 
        
        while (n > 0) {
            oneBitCount += n & 1; 
            if (oneBitCount >= 2) return false; 
            n = n >> 1;
        }
        
        return true; 
    }
}
