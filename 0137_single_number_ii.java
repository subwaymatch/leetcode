class Solution {
    public int singleNumber(int[] nums) {
        int target = 0; 
        
        for (int i = 0; i < 32; i ++) {
            int sum = 0; 
            
            for (int n : nums) {
                sum += (n >> i & 1);
            }
            
            if (sum % 3 != 0) {
                target |= 1 << i;
            }
        }
        
        return target; 
    }
}
