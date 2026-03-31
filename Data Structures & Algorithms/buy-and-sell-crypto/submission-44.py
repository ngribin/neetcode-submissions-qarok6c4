class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minV = float("inf")
        maxP = 0

        for p in prices:
            minV = min(minV, p)
            maxP = max(maxP, p - minV)

        return maxP
        