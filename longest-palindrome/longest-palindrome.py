class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        count = Counter(s)
        total = 0
        
        for element in count.values():
            
            total += element // 2 * 2
            
        
        return total if total == len(s) else total + 1
                