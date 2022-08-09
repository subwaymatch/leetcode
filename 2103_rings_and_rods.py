class Solution:
    def countPoints(self, rings: str) -> int:
        count_map = {}
        points = 0
        
        for i in range(0, len(rings), 2):
            color = rings[i]
            position = rings[i + 1]
            
            if position not in count_map:
                count_map[position] = set()
            
            count_map[position].add(color)
        
        for s in count_map.values():
            if s == { 'R', 'G', 'B' }:
                points += 1
                
        return points
