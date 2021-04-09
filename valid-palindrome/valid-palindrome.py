class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = s.lower()
        
        l = 0
        r = len(newString) - 1
        
        while l < r:
            if newString[l] != newString[r]:
                if not newString[l].isalnum():
                    l += 1
                elif not newString[r].isalnum():
                    r -= 1
                else:
                    return False
            
            else:
                l += 1
                r -= 1

        return True
        
        