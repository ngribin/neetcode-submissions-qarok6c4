class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_prof = 0

        for i in range(1, len(prices)):
            profit = prices[i] - prices[left]

            if profit > 0:
                max_prof=max(profit, max_prof)
            else:
                left = i

        return max_prof
                

        