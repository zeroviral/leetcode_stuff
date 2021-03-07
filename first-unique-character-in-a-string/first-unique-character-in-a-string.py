from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        lookup = defaultdict(list)
        
        for i in range(len(s)):
            if s[i] in lookup:
                lookup[s[i]][0] += 1
                lookup[s[i]][1] = i
            else:
                lookup[s[i]].append(1)
                lookup[s[i]].append(i)
        
        minIndex = float('inf')
        
        for value in lookup.values():
            if value[0] == 1:
                minIndex = min(minIndex, value[1])
        
        
        
        return -1 if minIndex == float('inf') else minIndex