class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            check = [False] * 10
            
            for v in row:
                if v != '.':
                    num = int(v)
                    if check[num]:
                        return False
                    
                    check[num] = True
        
        # Check cols
        for col in range(9):
            check = [False] * 10
            
            for row in range(9):
                if board[row][col] != '.':
                    num = int(board[row][col])
                    if check[num]:
                        return False
                
                    check[num] = True
        
        # Check 3x3 boards
        for box_row in range(3):
            for box_col in range(3):
                check = [False] * 10
                
                for row in range(box_row * 3, box_row * 3 + 3):
                    for col in range(box_col * 3, box_col * 3 + 3):
                        if board[row][col] != '.':
                            num = int(board[row][col])
                            if check[num]:
                                return False
                            
                            check[num] = True
            
        return True
                    
