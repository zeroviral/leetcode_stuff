class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                if not s[l].isalnum():
                    l += 1
                elif not s[r].isalnum():
                    r -= 1
                else:
                    return False
            
            else:
                l += 1
                r -= 1

        return True
        
        