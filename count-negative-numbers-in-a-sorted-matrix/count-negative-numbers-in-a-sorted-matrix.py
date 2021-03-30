class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        def binSearch(someList):
            l = 0
            r = len(someList) - 1
            
            while l <= r:
                mid = (l + r) // 2
                
                if someList[mid] < 0:
                    r = mid - 1
                else:
                    l = mid + 1
            return len(someList) - l
        
        return sum(binSearch(row) for row in grid)