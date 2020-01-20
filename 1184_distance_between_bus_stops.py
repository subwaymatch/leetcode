class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            temp = start
            start = destination
            destination = temp
        
        d1 = 0
        d2 = 0
        
        for i in range(len(distance)):
            if i >= start and i < destination:
                d1 = d1 + distance[i]
            else:
                d2 = d2 + distance[i]
        
        return min(d1, d2)
