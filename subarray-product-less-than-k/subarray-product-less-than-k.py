class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        currProd = 1
        
        for r in range(len(nums)):
            
            currProd *= nums[r]
            
            while currProd >= k and l <= r:
                currProd //= nums[l]
                l += 1
            
            count += r - l + 1
        return count