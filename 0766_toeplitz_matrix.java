class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return true; 
        
        for (int row = 0; row < matrix.length; row++) {
            int r = row; 
            int c = 0;
            
            int val = matrix[r][c]; 
           
            while (r < matrix.length && c < matrix[0].length) {
                if (val != matrix[r][c]) {
                    return false; 
                }
                val = matrix[r][c];
                
                r++; 
                c++; 
            }
        }
        
        for (int col = 0; col < matrix[0].length; col++) {
            int r = 0; 
            int c = col; 
            
            int val = matrix[r][c]; 
            
            while (r < matrix.length && c < matrix[0].length) {
                if (val != matrix[r][c]) {
                    return false; 
                }
                val = matrix[r][c];
                
                r++; 
                c++; 
            }
        }
        
        return true; 
    }
}
