class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        h = {0 : 1}

        for num in nums:
            curSum += num
            diff = curSum - k

            res += h.get(diff, 0)
            h[curSum] = 1+ h.get(curSum, 0)

        return res
        