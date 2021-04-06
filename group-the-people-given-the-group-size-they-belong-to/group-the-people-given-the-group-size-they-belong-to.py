from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
#         Put everything in a dictionary
#          Iterate through and then place everything inside each value list in a temp array.
#         once the len(tempArray) == key, we reset temp array.

        lookup = defaultdict(list)
        temp = []
        ans = []
        
        for i, item in enumerate(groupSizes):
            lookup[item].append(i)
        
        
        for key, values in lookup.items():
            for item in values:
                temp.append(item)
                if len(temp) == key:
                    ans.append(temp)
                    temp = []
        return ans