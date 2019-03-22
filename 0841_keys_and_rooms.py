class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        
        self.visit(rooms, 0, visited)
        
        return visited.count(True) == len(rooms)
    
    def visit(self, rooms: List[List[int]], idx: int, visited: List[int]) -> None:
        visited[idx] = True
        
        for key in rooms[idx]:
            if not visited[key]:
                self.visit(rooms, key, visited)
