class Solution {
    public int majorityElement(int[] nums) {
        int threshold = nums.length / 2;
        
        Map<Integer, Integer> countMap = new HashMap<Integer, Integer>(); 
        
        for (int num : nums) {
            if (countMap.containsKey(num)) {
                countMap.put(num, countMap.get(num) + 1); 
            }
            
            else {
                countMap.put(num, 1); 
            }
            
            if (countMap.get(num) > threshold) return num; 
        }
        
        return nums[0]; 
    }
}
