class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Lists to hold vertical/horizontal 1 counts
        
        hori = []
        vert = []
        dp = []
        
        if len(matrix) == 0:
            return 0
        
        max_width = int(matrix[0][0])
        
        # Build m x n matrix
        for row in range(len(matrix)):
            new_row = [0] * len(matrix[0])
            
            hori.append(new_row)
            vert.append(new_row.copy())
            dp.append(new_row.copy())
        
        # Build a list of horizontal 1 counter
        for row in range(len(matrix)):
            count = 0
            
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    count += 1
                else:
                    count = 0
            
                hori[row][col] = count
        
        # Build a list of vertical 1 counter
        for col in range(len(matrix[0])):
            count = 0
            
            for row in range(len(matrix)):
                if matrix[row][col] == "1":
                    count += 1
                else:
                    count = 0
                    
                vert[row][col] = count
        
        # Initialize dp
        for col in range(len(matrix[0])):
            dp[0][col] = int(matrix[0][col])
            
            max_width = max(dp[0][col], max_width)
        
        for row in range(len(matrix)):
            dp[row][0] = int(matrix[row][0])
            
            max_width = max(dp[row][0], max_width)
            
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                dp[row][col] = min(dp[row - 1][col - 1] + 1, hori[row][col], vert[row][col])
                
                max_width = max(dp[row][col], max_width)
                
        return max_width ** 2
