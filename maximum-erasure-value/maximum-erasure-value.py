class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        lookup = collections.defaultdict(int)
        maxVal = -math.inf
        currSum = 0
        
        for r in range(len(nums)):
            currSum += nums[r]
            
            lookup[nums[r]] += 1
            
            while l <= r and lookup[nums[r]] > 1:
                lookup[nums[l]] -= 1
                currSum -= nums[l]
                l += 1
            
            maxVal = max(maxVal, currSum)
        
        return maxVal