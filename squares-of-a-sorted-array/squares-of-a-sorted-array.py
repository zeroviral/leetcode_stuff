class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        
        ans = [None] * len(nums)
        l = 0
        r = size - 1
        
        for i in range(size - 1, -1, -1):
            if abs(nums[l]) < abs(nums[r]):
                nextElement = nums[r]
                r -= 1
            else:
                nextElement = nums[l]
                l += 1
            ans[i] = nextElement ** 2
        
        return ans