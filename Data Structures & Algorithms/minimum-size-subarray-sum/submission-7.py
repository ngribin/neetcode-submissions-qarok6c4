class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minV = float("inf")
        total = 0
        left = 0

        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                minV = min(minV, i - left + 1)
                total -= nums[left]
                left += 1

        return minV if minV < float("inf") else 0
        