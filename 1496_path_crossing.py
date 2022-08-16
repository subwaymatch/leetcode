class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = { (0, 0) }
        coord = [0, 0]
        direction_dict = { 'N': [-1, 0], 'S': [1, 0], 'E': [0, 1], 'W': [0, -1] }
        
        for c in path:
            direction = direction_dict[c]
            coord[0] += direction[0]
            coord[1] += direction[1]
            coord_tuple = tuple(coord)
            
            if coord_tuple in visited:
                return True
            else:
                visited.add(coord_tuple)
        
        return False
