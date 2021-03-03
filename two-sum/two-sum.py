class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lookup = {}
        
        for i, element in enumerate(nums):
            
            if target - element in lookup:
                return [lookup[target - element], i]
            else:
                lookup[element] = i
        