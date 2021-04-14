class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        lookup = collections.defaultdict(int)
        ans = []        
        for i in range(len(arr1)):
            lookup[arr1[i]] += 1
            lookup[arr2[i]] += 1
            lookup[arr3[i]] += 1
        
        for key, value in lookup.items():
            if value == 3:
                ans.append(key)
        return ans
        