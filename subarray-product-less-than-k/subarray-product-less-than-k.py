class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        currProd = 1
        
        for r in range(len(nums)):
            
            currProd *= nums[r]
            
            while l <= r and currProd >= k:
                currProd //= nums[l]
                l += 1
            
            if currProd < k:
                count += r - l + 1
        return count