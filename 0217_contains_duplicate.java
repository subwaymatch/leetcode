public class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Boolean> checkMap = new HashMap<Integer, Boolean>(); 
        
        for (int num : nums) {
            if (checkMap.containsKey(num)) return true; 
            checkMap.put(num, true); 
        }
        
        return false; 
    }
}
