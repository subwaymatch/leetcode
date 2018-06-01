class Solution {
    int numRows; 
    int numCols; 
    char[][] board; 
    String word; 
    boolean[][] visited; 
    
    public boolean exist(char[][] board, String word) {
        numRows = board.length; 
        numCols = board[0].length; 
        this.board = board; 
        this.word = word; 
        visited = new boolean[numRows][numCols];
        
        for (int row = 0; row < numRows; row++) {
            for (int col = 0; col < numCols; col++) {
                if (search(0, row, col) == true) return true; 
            }
        }
        
        return false; 
    }
    
    boolean search(int currentIndex, int row, int col) {
        if (currentIndex == word.length()) return true; 
        else if (row >= numRows) return false; 
        else if (row < 0) return false; 
        else if (col >= numCols) return false; 
        else if (col < 0) return false; 
        else if (visited[row][col] == true) return false; 
        
        char c = board[row][col]; 
        
        if (c == word.charAt(currentIndex)) {
            visited[row][col] = true; 

            if (search(currentIndex + 1, row - 1, col) == true) return true; 
            else if (search(currentIndex + 1, row, col - 1) == true) return true; 
            else if (search(currentIndex + 1, row + 1, col) == true) return true; 
            else if (search(currentIndex + 1, row, col + 1) == true) return true; 

            visited[row][col] = false; 
        }
        
        return false; 
    }
}
