class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = res = 0

        for num in nums:
            count += 1 if num else - count
            res = max(count, res)

        return res