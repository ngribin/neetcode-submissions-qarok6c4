class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        left_p = 1
        for i in range(n):
            res[i] *= left_p
            left_p *= nums[i]

        right_p = 1

        for i in range(n - 1, - 1, - 1):
            res[i] *= right_p
            right_p *= nums[i]

        return res