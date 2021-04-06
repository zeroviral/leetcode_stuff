class Solution:
    def findCircleNum(self, A):
        seen = set()
        def dfs(node):
            for curr, nxt in enumerate(A[node]):
                if nxt and curr not in seen:
                    seen.add(curr)
                    dfs(curr)

        ans = 0
        for i in range(len(A)):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans