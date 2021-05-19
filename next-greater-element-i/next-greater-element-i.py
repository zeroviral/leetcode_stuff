class Solution:
    def nextGreaterElement(self, findNums: List[int], nums: List[int]) -> List[int]:
        stack = []
        lookup = collections.defaultdict(int)
        ans = []
        
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1]:
                lookup[stack.pop()] = nums[i]
            stack.append(nums[i])
        
        while stack:
            lookup[stack.pop()] = -1
        for i in range(len(findNums)):
            ans.append(lookup[findNums[i]])
        return ans