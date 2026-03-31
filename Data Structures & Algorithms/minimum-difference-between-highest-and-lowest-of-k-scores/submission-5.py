class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        left, right = 0, k - 1
        minV = float("inf")

        while right < len(nums):
            minV = min(minV, nums[right] - nums[left])
            left += 1
            right += 1

        return minV
        
