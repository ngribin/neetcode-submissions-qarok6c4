class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minV = float("inf")
        left = 0
        right = k - 1

        while right < len(nums):
            minV = min(minV, nums[right] - nums[left])
            left += 1
            right += 1

        return minV