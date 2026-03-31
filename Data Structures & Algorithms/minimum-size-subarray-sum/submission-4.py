class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minV = float("inf")
        summ = 0
        left = 0    

        for i in range(len(nums)):
            summ += nums[i]

            while summ >= target:
                minV = min(minV, i - left + 1)
                summ -= nums[left]
                left += 1
                

        return minV  if minV < float("inf") else 0      