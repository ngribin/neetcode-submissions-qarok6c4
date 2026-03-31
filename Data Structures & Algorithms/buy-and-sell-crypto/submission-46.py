class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minP = float("inf")

        for p in prices:
            minP = min(p, minP)
            maxP = max(maxP, p - minP)

        return maxP
            

        