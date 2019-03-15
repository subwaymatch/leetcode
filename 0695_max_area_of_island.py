class Solution:
    def __init__(self):
        self.visited = []
        self.grid = []
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        self.grid = grid
        
        if len(grid) == 0:
            return 0
        
        for row in grid:
            pass
        
        for row in range(len(grid)):
            self.visited.append([False] * len(grid[0]))
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if not self.visited[row][col]:
                    if grid[row][col] == 0:
                        self.visited[row][col] = True
                    else:
                        max_area = max(max_area, self.run_bfs(row, col))
        
        return max_area
    

    def run_bfs(self, row, col):
        area = 0
        next_coords = [(row, col)]
        
        while next_coords:
            new_next_coords = []

            for coords in next_coords:
                row = coords[0]
                col = coords[1]
                
                if not self.visited[row][col] and self.grid[row][col] == 1:
                    self.visited[row][col] = True
                    area += 1
                    
                    if row > 0:
                        new_next_coords.append((row - 1, col))
                    if row < len(self.grid) - 1:
                        new_next_coords.append((row + 1, col))
                    if col > 0:
                        new_next_coords.append((row, col - 1))
                    if col < len(self.grid[0]) - 1:
                        new_next_coords.append((row, col + 1))
                        
            
            next_coords = new_next_coords
        
        return area
