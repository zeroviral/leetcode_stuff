class Solution:
    def removeVowels(self, s: str) -> str:
        seen = set("aeiou")
        finalString = ""
        for c in s:
            if c not in seen:
                finalString += c
        return finalString
        