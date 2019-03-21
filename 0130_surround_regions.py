# 1: Start on the 'O' slots on the border and mark all connected 'O's to 'B'
# 2: Second pass to mark all remaining 'O's as 'X's and 'B's to 'O'

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) <= 1 or len(board[0]) <= 1:
            return
        
        """
        Do not return anything, modify board in-place instead.
        """
        for row in range(len(board)):
            if board[row][0] == 'O':
                self.find_dfs(board, row, 0)
            if board[row][len(board[0]) - 1] == 'O':
                self.find_dfs(board, row, len(board[0]) - 1)
                
        for col in range(1, len(board[0]) - 1):
            if board[0][col] == 'O':
                self.find_dfs(board, 0, col)
            if board[len(board) - 1][col] == 'O':
                self.find_dfs(board, len(board) - 1, col)
                
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != 'X':
                    board[row][col] = 'O' if board[row][col] == 'B' else 'X'
        
    def find_dfs(self, board, row, col):
        board[row][col] = 'B'
        
        if row < len(board) - 1 and (board[row + 1][col] != 'X' and board[row + 1][col] != 'B'):    
            self.find_dfs(board, row + 1, col)
        if row > 0 and (board[row - 1][col] != 'X' and board[row - 1][col] != 'B'):
            self.find_dfs(board, row - 1, col)
        
        
        if col < len(board[0]) - 1 and (board[row][col + 1] != 'X' and board[row][col + 1] != 'B'):    
            self.find_dfs(board, row, col + 1)
        if col > 0 and (board[row][col - 1] != 'X' and board[row][col - 1] != 'B'):
            self.find_dfs(board, row, col - 1)
