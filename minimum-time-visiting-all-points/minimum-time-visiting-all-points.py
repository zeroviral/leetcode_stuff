class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        '''
        We need: time
        
        1. We use this formula for each point, within points up until the index (len(points) - 1)
        
        (4 - 1) // (3 - 1) -> 1.5 * (X2 - X1)
        
        Better written as...
        
        ((y2 - y1) / (x2 - x1)) * abs(x2 - x1)
        '''
        ans = 0
        for i in range(1, len(points)):
            prev, cur = points[i - 1 : i + 1]
            ans += max(map(abs, (prev[0] - cur[0], prev[1] - cur[1])))
        return ans    