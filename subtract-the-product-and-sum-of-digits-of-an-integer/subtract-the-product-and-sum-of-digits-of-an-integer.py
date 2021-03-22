class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        string = str(n)
        stringVals = [c for c in string]
        sumVal, product = 0, 1
        for element in stringVals:
            product *= int(element)
            sumVal += int(element)
        return product - sumVal