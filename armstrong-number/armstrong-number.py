class Solution:
    def isArmstrong(self, n: int) -> bool:
        x = str(n)
        target = sum([int(i) ** len(x) for i in x])
        return target == n
        