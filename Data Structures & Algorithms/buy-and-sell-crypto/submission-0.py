class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        minPrice = prices[0]

        for i,x in enumerate(prices):
            minPrice = min(minPrice,x)
            maxProfit = max(x-minPrice,maxProfit)

        return maxProfit

        