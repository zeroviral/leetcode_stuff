from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = [0 for i in range(1001)]
        
        def dfs(rooms, room, visited):
            visited[room] = 1
            
            for key in rooms[room]:
                if visited[key] == 0:
                    dfs(rooms, key, visited)
                
        dfs(rooms, 0, visited)
        for i in range(len(rooms)):
            if visited[i] == 0:
                return False
            
        return True
                