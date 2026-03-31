class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minV= float("inf")
        left, right = 0, k - 1

        while right < len(nums):
            minV = min(minV, nums[right] - nums[left])
            right += 1
            left += 1

        return minV

        