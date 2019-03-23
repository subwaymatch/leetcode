class Solution {
    public int[][] generateMatrix(int n) {
        int[][] mat = new int[n][n];
        
        int leftRows = n;
        int leftCols = n;

        // 0 = right, 1 = down, 2 = left, 3 = up
        int direction = 0;
        
        int row = 0;
        int col = 0;
        
        int num = 1;
        int lineFilled = 0;

        while (num <= n * n) {
            mat[row][col] = num++;
            lineFilled++;
            
            switch (direction) {
                case 0:
                    if (lineFilled == leftCols) {
                        leftRows--;
                        direction++;
                        row++;
                        lineFilled = 0;
                    }
                    else {
                        col++;
                    }
                    
                    break;
                    
                case 1:
                    if (lineFilled == leftRows) {
                        leftCols--;
                        direction++;
                        col--;
                        lineFilled = 0;
                    } else {
                        row++;
                    }
                    
                    break;
                case 2:
                    if (lineFilled == leftCols) {
                        leftRows--;
                        direction++;
                        row--;
                        lineFilled = 0;
                    }
                    else {
                        col--;
                    }
                    
                    break;
                case 3:
                    if (lineFilled == leftRows) {
                        leftCols--;
                        direction = (direction + 1) % 4;
                        col++;
                        lineFilled = 0;
                    } else {
                        row--;
                    }
                    
                    break;
            }
        }
        
        return mat; 
    }
}
