class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        travel_distance = 0
        first_nut_diff = sys.maxsize
    
        for nut in nuts:
            distance_from_tree = abs(tree[0] - nut[0]) + abs(tree[1] - nut[1])
            distance_from_squirrel = abs(squirrel[0] - nut[0]) + abs(squirrel[1] - nut[1])
            
            travel_distance += distance_from_tree * 2
            
            diff = distance_from_squirrel - distance_from_tree
            
            if diff < first_nut_diff:
                first_nut_diff = diff
            
        return travel_distance + first_nut_diff
