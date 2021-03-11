class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        l, s = len(nums), sum(set(nums))
        l = l * ( 1 + l ) // 2
        return [sum(nums) - s, l - s]