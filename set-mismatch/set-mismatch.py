from collections import Counter
from collections import defaultdict

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)
        lookup = defaultdict()
        dupe, missing = 0, 0
        
        for i in range(1, len(nums) + 1):
            lookup[i] = 1
        
        for i in range(len(nums)):
            
            if count[nums[i]] > 1:
                dupe = nums[i]
            
        
        for key in lookup.keys():
            if key not in count:
                missing = key
                break
                
            
        return [dupe, missing]
                