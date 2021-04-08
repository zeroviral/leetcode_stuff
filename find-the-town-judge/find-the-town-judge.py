class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        indeg = [0] * (N + 1) 
        outdeg = [0] * (N + 1)
        for person, trusts in trust:
            indeg[trusts] += 1
            outdeg[person] += 1
        for i in range(1, N + 1):
            if indeg[i] == N - 1 and outdeg[i] == 0:
                return i
        return -1