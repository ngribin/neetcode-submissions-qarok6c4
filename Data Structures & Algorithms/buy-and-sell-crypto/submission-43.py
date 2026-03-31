class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        maxP = 0

        for p in prices:
            min_price = min(min_price, p)
            maxP = max(maxP, p - min_price)        

        return maxP