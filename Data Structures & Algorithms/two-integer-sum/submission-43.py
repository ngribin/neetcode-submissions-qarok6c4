class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i, num in enumerate(nums):
            temp = target - nums[i]

            if temp in h:
                return [h[temp], i]


            h[num] = i 

        return []