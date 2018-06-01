class Solution {
    public boolean isHappy(int n) {
        if (n == 0) return false; 
        else if (n == 1 || n == 7) return true; 
        else if (n <= 9) return false;
            
        int result = 0; 
     
        while (n >= 1) {
            result += (n % 10) * (n % 10); 
            n /= 10; 
        }
        
        return isHappy(result); 
    }
}
