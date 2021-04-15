class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = pre = 0
        for item in target:
            res += max(item - pre, 0)
            pre = item
        return res