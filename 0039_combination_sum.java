public class Solution {
    private void findCombination(int[] candidates, int startIndex, List<Integer> combination, int diff, List<List<Integer>> combinations) {
        if (diff == 0) {
            combinations.add(combination); 
            return; 
        }
        
        for (int i = startIndex; i < candidates.length; i++) {
            int num = candidates[i]; 
            
            if (num <= diff) {
                List<Integer> newCombination = new ArrayList<Integer>(); 
                
                for (Integer val : combination) {
                    newCombination.add(val); 
                }
                
                newCombination.add(num); 
                
                findCombination(candidates, i, newCombination, diff - num, combinations); 
            }
        }
    }
    
    public List<List<Integer>> combinationSum(int[] candidates, int target)  {
        List<List<Integer>> combinations = new ArrayList<List<Integer>>(); 
        
        for (int i = 0; i < candidates.length; i++) {
            int num = candidates[i]; 
            
            if (num <= target) {
                List<Integer> combination = new ArrayList<Integer>(); 
                combination.add(num); 
                
                findCombination(candidates, i, combination, target - num, combinations); 
            }
        }
    
        return combinations; 
    }
}
