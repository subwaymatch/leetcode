class Solution {
    public boolean hasAlternatingBits(int n) {
        int num = n;
        int prev_bit = (num & 1) ^ 1;
        
        while (num > 0) {
            int new_bit = num & 1;
            
            if (new_bit == prev_bit) return false; 
            prev_bit = new_bit;
            num = num >> 1;
        }
        
        return true; 
    }
}
