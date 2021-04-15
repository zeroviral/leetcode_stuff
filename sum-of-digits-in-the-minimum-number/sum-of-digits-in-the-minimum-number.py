class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        return int(sum([int(c) for c in str(min(A))]) % 2 == 0)