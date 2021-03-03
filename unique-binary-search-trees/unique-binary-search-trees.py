class Solution:
    def numTrees(self, n: int) -> int:
        
        C = 1
        for i in range(n):
            C *= 2 * (2 * i + 1) / (i + 2)
        
        return int(C)