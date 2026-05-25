class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxV = 0
        minV = float("inf")

        for p in prices:
            minV = min(minV, p)
            maxV = max(maxV, p - minV)

        return maxV