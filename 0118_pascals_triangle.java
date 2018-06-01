class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> returnRows = new ArrayList<List<Integer>>(); 
        List<Integer> prevRow = null; 
        
        for (int i = 1; i <= numRows; i++) {
            List<Integer> row = new ArrayList<Integer>(); 
            
            row.add(1); 
            
            for (int j = 1; j < i - 1; j++) {
                row.add(prevRow.get(j - 1) + prevRow.get(j)); 
            }
            
            if (i > 1) row.add(1); 
            
            returnRows.add(row); 
            prevRow = row; 
        }
        
        return returnRows;
    }
}
