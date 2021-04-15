class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        l, minVal, spot = 0, math.inf, -1
        
        while l < len(points):
            a, b = points[l]
            if a == x or b == y:
                manhattan = abs(a - x) + abs(b - y)
                if manhattan < minVal:
                    minVal, spot = manhattan, l
            l += 1
        return spot