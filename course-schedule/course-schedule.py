class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapper = defaultdict(list)
        
        for secondtask, firsttask  in prerequisites:
            mapper[secondtask].append(firsttask)
			
        track = set()
		
        def dfs (crs):
            if crs in track:
                return False
            
            if not mapper[crs]:
                return True
				
            track.add(crs)
			
            for i in mapper[crs]:
                
                if not dfs(i): 
                    return False
					
            mapper[crs]=[] 
			
            track.remove(crs)
            return True 
			
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True 