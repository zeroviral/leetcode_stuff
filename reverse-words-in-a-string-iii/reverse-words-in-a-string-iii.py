class Solution:
    def reverseWords(self, s: str) -> str:
        values = s.split(" ")
        ans = []
        for i, val in enumerate(values):
            ans.append(val[::-1])
        return " ".join(ans)
        