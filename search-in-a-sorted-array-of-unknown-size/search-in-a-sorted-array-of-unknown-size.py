# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        l = 0
        r = 1
        
        while reader.get(r) < target:
            l = r
            r <<= 2
        
        
        while l <= r:
            mid = (l + r) // 2
            
            if reader.get(mid) == target:
                return mid
            if reader.get(mid) > target:
                r = mid - 1
            else:
                l = mid + 1
            
                
        return l if reader.get(l) == target else -1