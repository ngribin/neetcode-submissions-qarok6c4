class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        max_prof = 0

        for i in range(len(prices)):
            profit =prices[i] - prices[start]
            if profit > 0:
                max_prof = max(profit, max_prof)

            else:
                start = i
        return max_prof        