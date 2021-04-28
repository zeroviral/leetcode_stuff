class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = set()
        
        def dfs(combo, opens, closed):
            if len(combo) == (2 * n):
                ans.add("".join(combo))
                return
            if opens < n:
                combo.append("(")
                dfs(combo, opens + 1, closed)
                combo.pop()
            if closed < opens:
                combo.append(")")
                dfs(combo, opens, closed + 1)
                combo.pop()
        
        dfs([], 0, 0)
        return list(ans)