class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        for right in range(1, len(nums)):
            left = right
            while left > 0 and nums[left] < nums[left - 1]:
                nums[left - 1], nums[left] = nums[left], nums[left - 1]
                left -= 1

        return nums
        