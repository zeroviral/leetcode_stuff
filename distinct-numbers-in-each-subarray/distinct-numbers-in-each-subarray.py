class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        count = 0
        l = 0
        ans = []
        lookup = collections.defaultdict(int)
        
        for r in range(len(nums)):
            lookup[nums[r]] += 1
            
            if lookup[nums[r]] == 1:
                count += 1
            
            while r - l + 1 > k:
                lookup[nums[l]] -= 1
                
                if lookup[nums[l]] < 1:
                    count -= 1
                l += 1
            
            if r - l + 1 == k:
                ans.append(count)
            
        return ans