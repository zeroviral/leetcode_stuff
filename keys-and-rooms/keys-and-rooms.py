class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        targetRoom = len(rooms) - 1
        
        visited = set()
        
        
        def dfs(node):
            visited.add(node)

            for key in rooms[node]:
                if key not in visited:
                    dfs(key)
        
        dfs(0)
        
        return len(visited) == len(rooms)