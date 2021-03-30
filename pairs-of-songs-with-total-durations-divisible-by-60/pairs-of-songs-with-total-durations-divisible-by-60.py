from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        lookup = defaultdict(int)
        for element in time:
            if element % 60 == 0:
                count += lookup[0]
            else:
                count += lookup[60 - element % 60]
            lookup[element % 60] += 1
        return count