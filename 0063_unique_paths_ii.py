class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        num_rows = len(obstacleGrid)
        num_cols = len(obstacleGrid[0])
        
        dp = []
        for idx in range(num_rows):
            dp.append([0] * num_cols)
        
        dp[0][0] = 1 - obstacleGrid[0][0]
        
        for col in range(1, num_cols):
            dp[0][col] = 0 if obstacleGrid[0][col] == 1 else dp[0][col - 1]
        
        for row in range(1, num_rows):
            dp[row][0] = 0 if obstacleGrid[row][0] == 1 else dp[row - 1][0]
        
        for row in range(1, num_rows):
            for col in range(1, num_cols):
                dp[row][col] = 0 if obstacleGrid[row][col] == 1 else dp[row - 1][col] + dp[row][col - 1]
        
        return dp[-1][-1]
