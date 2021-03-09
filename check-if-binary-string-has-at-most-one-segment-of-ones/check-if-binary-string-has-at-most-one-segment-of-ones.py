class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        segments = 0
        
        for i in range(len(s) - 1):
            if s[i + 1] == "0" and s[i] == "1" or s[i + 1] == "1" and s[i] == "0":
                segments +=1

        return segments <= 1