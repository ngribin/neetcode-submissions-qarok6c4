class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        miv = float('inf')
        mav = 0

        for p in prices:
            miv = min(miv, p)
            mav = max(mav, p - miv)

        return mav