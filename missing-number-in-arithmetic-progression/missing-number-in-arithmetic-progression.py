class Solution:
    def missingNumber(self, A):
        return int((min(A) + max(A)) * (len(A) + 1) / 2 - sum(A))
