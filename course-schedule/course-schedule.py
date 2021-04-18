class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegree = {i:0 for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        sources = [course for course in indegree if indegree[course] == 0]  
        ans = []
        
        while sources:
            prereq = sources.pop()
            ans.append(prereq)
            for course in graph[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    sources.append(course)
        
        return len(ans) == numCourses