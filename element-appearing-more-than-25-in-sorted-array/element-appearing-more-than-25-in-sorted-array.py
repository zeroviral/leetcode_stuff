class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        lookup = Counter(arr)
        maxVal = max(lookup.values())
        return next(key for key, value in lookup.items() if value == maxVal)