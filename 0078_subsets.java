class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> listOfNums = new ArrayList<List<Integer>>(); 
        
        listOfNums.add(new ArrayList<Integer>()); 
        
        for (int num : nums) {
            int listOfNumsLength = listOfNums.size(); 
            
            for (int i = 0; i < listOfNumsLength; i++) {
                List<Integer> list = listOfNums.get(i); 
                
                List<Integer> newList = new ArrayList<Integer>(list); 
                newList.add(num); 
                
                listOfNums.add(newList); 
            }
        }
        
        return listOfNums; 
    }
}
