class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length; 
        if (m == 0) return 0; 
        int n = grid[0].length; 
        if (n == 0) return 0; 
        
        int[][] dpTable = new int[m][n]; 
        dpTable[0][0] = grid[0][0]; 
        
        for (int j = 1; j < m; j++) dpTable[j][0] = dpTable[j - 1][0] + grid[j][0]; 
        for (int i = 1; i < n; i++) dpTable[0][i] = dpTable[0][i - 1] + grid[0][i]; 
        
        for (int j = 1; j < m; j++) {
            for (int i = 1; i < n; i++) {
                dpTable[j][i] = Math.min(dpTable[j - 1][i], dpTable[j][i - 1]) + grid[j][i]; 
            }
        }
        
        return dpTable[m - 1][n - 1]; 
    }
}
