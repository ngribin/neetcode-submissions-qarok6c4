class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = h.get(nums[i], 0) + 1


        return [num for num, val in h.items() if val > len(nums) //3 ]