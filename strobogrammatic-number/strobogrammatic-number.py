class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        maps = {
            ("0", "0"),
            ("6", "9"),
            ("9", "6"),
            ("8", "8"),
            ("1", "1")
        }
        
        l = 0
        r = len(num) - 1
        while l <= r:
            if (num[l], num[r]) not in maps:
                return False
            l += 1
            r -= 1
        return True