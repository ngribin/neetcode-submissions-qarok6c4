class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0
        for i in range(len(prices)):
            profit = prices[i] - prices[left]
            if profit > 0:
                max_profit = max(max_profit, profit)
               

            else:   
                left = i
        return max_profit