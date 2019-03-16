class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points_distances = []
        
        for point in points:
            points_distances.append((point, point[0] ** 2 + point[1] ** 2))
        
        points_distances = sorted(points_distances, key=lambda x: x[1])
        
        return list(map(lambda x: x[0], points_distances[:K]))
