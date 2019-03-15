class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = []
        max_width = 0
        
        for row in range(len(matrix)):
            dp.append([0] * len(matrix[0]))
            
            for col in range(len(matrix[0])):
                if row == 0 or col == 0 or matrix[row][col] == '0':
                    dp[row][col] = int(matrix[row][col])
                else:
                    dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1]) + 1
                    
                max_width = max(dp[row][col], max_width)
                
        for row in dp:
            pass
        
        return max_width ** 2
