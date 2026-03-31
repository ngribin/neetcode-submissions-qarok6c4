class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        min_len = nums[0]
        while left <= right:
            mid = (left + right) // 2
            min_len = min(nums[mid], min_len)
            if nums[mid] >= nums[right]:
                left = mid + 1

            else:
                right  = mid - 1   
        return min_len