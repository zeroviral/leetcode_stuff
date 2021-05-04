class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        index = 0
        spaces = 0
        
        while index < len(s) and spaces < k:
            if s[index] == " ":
                spaces += 1
            index += 1
        return s[:index - 1] if index < len(s) else s[:index]