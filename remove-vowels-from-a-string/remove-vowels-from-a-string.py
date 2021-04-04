class Solution:
    def removeVowels(self, s: str) -> str:
        finalString = ""
        for c in s:
            if c not in "aeiou":
                finalString += c
        return finalString
        