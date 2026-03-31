class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minV = float("inf")
        maxV = 0

        for p in prices:
            minV = min(minV, p)
            maxV = max(maxV, p - minV)
        return maxV