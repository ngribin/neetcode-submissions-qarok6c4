class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_num = float("inf")
        left = 0
        summ = 0

        for r in range(len(nums)):
            summ += nums[r] 


            while summ >= target:
                min_num = min(min_num, r - left + 1)
                summ -= nums[left]
                left += 1    


        return min_num if min_num < float("inf") else 0        