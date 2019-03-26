class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.count = {
            1: {
                "rows": [0] * n,
                "cols": [0] * n,
                "diag1": 0,
                "diag2": 0
            },
            2: {
                "rows": [0] * n,
                "cols": [0] * n, 
                "diag1": 0,
                "diag2": 0
            }
        }
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        player_count = self.count[player]
        
        player_count["rows"][row] += 1
        player_count["cols"][col] += 1
        
        if row == col:
            player_count["diag1"] += 1
        if row == self.n - col - 1:
            player_count["diag2"] += 1
        
        if player_count["rows"][row] == self.n or player_count["cols"][col] == self.n or player_count["diag1"] == self.n or player_count["diag2"] == self.n:
            return player
        
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
