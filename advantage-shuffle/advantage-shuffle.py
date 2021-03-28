class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        a = sorted(A)
        for i in range(len(B)):
            index = bisect.bisect_right(a, B[i])
            if index == len(a):
                index = 0
            A[i] = a[index]
            a.pop(index)
        return A