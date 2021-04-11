class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = [0 for i in range(1000)]
        
        def dfs(room, visited):
            visited[room] = 1
            
            for key in rooms[room]:
                if visited[key] == 0:
                    dfs(key, visited)
                
        dfs(0, visited)
        for i in range(len(rooms)):
            if visited[i] == 0:
                return False
            
        return True