class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
#         pre = [i for i in range(len(nums) + 1)]
#         pre[0] = 1
        
#         for i in range(1, len(nums)):
#             pre[i] = nums[i] + nums[i - 1]
      
        sum = 0
        res = 0
        hashmap = {0 : -1}
        for i in range(len(nums)):
            sum += nums[i]
            if -(k - sum) in hashmap:
                res = max(res, i - hashmap[-(k - sum)])
            if sum not in hashmap:
                hashmap[sum] = i
        return res