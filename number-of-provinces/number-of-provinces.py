class Solution:
    def findCircleNum(self, A):
        seen = set()
        def dfs(node):
            for nei, adj in enumerate(A[node]):
                print(f'nei is now: {nei}')
                if adj and nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        ans = 0
        for i in range(len(A)):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans