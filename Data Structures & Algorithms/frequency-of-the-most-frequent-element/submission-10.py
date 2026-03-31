class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        total = res = 0
        left = 0


        for i in range(len(nums)):
            total += nums[i]

            while nums[i] * (i-left + 1) > total + k:
                total -= nums[left]
                left += 1


            res = max(res, i - left + 1)

        return res
        