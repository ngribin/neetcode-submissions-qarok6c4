class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h = {}


        for i in range(len(nums)):
            h[nums[i]] = h.get(nums[i], 0) + 1

        limit = len(nums) // 3
        

        return [key for key,  val in h.items() if val > limit]
        