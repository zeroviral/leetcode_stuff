class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:

            mid = l + (r - l) // 2

            count = nums[mid] - nums[0] - mid

            if count > k:
                r = mid - 1
            elif count < k:
                l = mid + 1
            else:
                return nums[mid] - 1

        return k + nums[0] + l - 1