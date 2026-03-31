class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        min_price = prices[0]

        for p in prices:
            min_price = min(min_price, p)
            max_price = max(max_price, p - min_price)

        return max_price