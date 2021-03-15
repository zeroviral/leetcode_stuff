class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        if len(s1) == 1:
            return False
        
        lookup = {}
        
        for element in s1:
            lookup[element] = 1
        
        count = 0
        
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                if s2[i] not in lookup:
                    return False
                count += 1
        return True if count <= 2 else False