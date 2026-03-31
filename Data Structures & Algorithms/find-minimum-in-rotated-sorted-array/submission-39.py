class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        minV = float("inf")

        while left <= right:
            mid = (left + right) // 2
            minV = min(minV, nums[mid])

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return minV 


        