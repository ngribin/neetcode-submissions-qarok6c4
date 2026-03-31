class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        max_val = max(count, key=count.get)

        return max_val
        