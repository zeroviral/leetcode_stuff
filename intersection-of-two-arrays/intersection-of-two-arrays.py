class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = Counter(nums1)
        
        ans = set()
        
        for element in nums2:
            if element in lookup:
                ans.add(element)
        
        return ans