class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b = s[:len(s) // 2].lower(), s[len(s) // 2:].lower()
        countA, countB = 0, 0
        
        for i in range(len(a)):
            if a[i] in "aeiou": countA += 1
            if b[i] in "aeiou": countB += 1
        return countA == countB