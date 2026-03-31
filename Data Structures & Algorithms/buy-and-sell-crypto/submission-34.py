class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0

        for i in range(len(prices)):
            profit = prices[i] - prices[l]
            
            if profit > 0:
                max_profit = max(profit, max_profit)

            else:
                l = i

        return max_profit    