from collections import OrderedDict

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        ans = l = 0
        # Last seen index of an integer
        od = OrderedDict()
        for i, n in enumerate(A):
            od[n] = i
            od.move_to_end(n)
            while len(od) > K:
                l = od.popitem(last=False)[1] + 1
            if len(od) == K:
			    # The smallest index in od - left bound + 1
                ans += next(iter(od.items()))[1] - l + 1
        return ans