class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        min_price = prices[0]
        left = 0
        for p in prices:
            min_price = min(min_price, p)
            maxP = max(maxP, p - min_price)

        return maxP
        