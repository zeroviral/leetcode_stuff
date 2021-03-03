class Solution:
    def removeVowels(self, s: str) -> str:
        lookup = {
            "a" : 1,
            'e' : 1,
            'i' : 1,
            'o' : 1,
            'u' : 1
        }
        
        
        
        
        return "".join([element for element in s if element not in lookup])
        