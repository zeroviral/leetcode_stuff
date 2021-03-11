class Solution:
    def countLetters(self, S: str) -> int:
        total = 1
        count = 1
        for i in range(1, len(S)):
            if S[i] == S[i-1]:
                count += 1
            else:
                count = 1
            total += count
        return total