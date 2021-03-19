class Solution:
    def hammingWeight(self, n: int) -> int:
        
        val = "{0:b}".format(n)
        
        return len([int(element) for element in val if element == "1"])
        