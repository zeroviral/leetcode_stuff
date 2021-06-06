class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l, r = 0, 0
        maxLength = 0
        currMin = math.inf
        currMax = -math.inf
        
        
        while l <= r and r < len(nums):
            currMax = max(currMax, nums[r])
            currMin = min(currMin, nums[r])
            
            if currMax - currMin <= limit:
                maxLength = max(maxLength, r - l + 1)
            
            else:
                if currMax == nums[l]:
                    currMax = max(nums[l + 1 : r + 1])
                elif currMin == nums[l]:
                    currMin = min(nums[l + 1 : r + 1])
                l += 1
            
            r += 1
        return maxLength
                