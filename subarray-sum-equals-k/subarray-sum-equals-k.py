class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        lookup = collections.defaultdict(int)
        lookup[0] = 1
        count = 0
        currSum = 0

        for num in nums:
            currSum += num

            if currSum - k in lookup:
                count += lookup[currSum - k]
            
            lookup[currSum] += 1
            
        return count