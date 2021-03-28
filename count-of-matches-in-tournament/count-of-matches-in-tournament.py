class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        matches = 0
        teams = n
        while teams > 1:
            matches += (teams // 2)
            teams = (teams // 2) + (teams % 2)
        return matches