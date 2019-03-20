class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if len(rooms) == 0 or len(rooms[0]) == 0: 
            return
        
        coords = []
        new_coords = []
        INF = 2147483647
        
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    coords.append((row, col))
        
        distance = 0
        while len(coords) > 0:
            coord = coords.pop(0)
            row = coord[0]
            col = coord[1]

            if row < 0 or row >= len(rooms) or col < 0 or col >= len(rooms[0]):
                pass
            elif rooms[row][col] > 0 and rooms[row][col] < INF:
                pass
            elif rooms[row][col] != INF and distance > 0:
                pass
            else:
                rooms[row][col] = distance
                new_coords.extend([(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)])
            
            if len(coords) == 0:
                coords = new_coords
                new_coords = []
                distance += 1
