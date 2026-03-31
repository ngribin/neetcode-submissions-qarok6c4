class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = float("inf")
        maxP = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            else:
                left = right
            right += 1

        return maxP