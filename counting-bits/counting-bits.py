class Solution:
    def countBits(self, num: int) -> List[int]:
        return [len([ones for ones in bin(i)[2:] if ones=='1']) for i in range(num + 1)]