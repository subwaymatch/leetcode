class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total_diameter = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    total_diameter += 4
                    
                    if row > 0 and grid[row - 1][col] == 1:
                        total_diameter -= 1
                    
                    if col > 0 and grid[row][col - 1] == 1:
                        total_diameter -= 1
                    
                    if row < len(grid) - 1 and grid[row + 1][col] == 1:
                        total_diameter -= 1
                    
                    if col < len(grid[0]) - 1 and grid[row][col + 1] == 1:
                        total_diameter -= 1
                
        return total_diameter
