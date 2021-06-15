class Solution:
    def maxProfit(self, prices):
        minPrice = math.inf
        maxProfit = 0
        
        for price in prices:
            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
        return maxProfit