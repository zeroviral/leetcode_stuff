class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        
        x, y, z = 0, 1, 1
        
        for _ in range(n - 2):
            x, y, z = y, z, x + y + z
        return z