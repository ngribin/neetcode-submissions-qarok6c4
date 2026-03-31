class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            indices[num] = i

        for i, num in enumerate(nums):
            dif = target - num
            if dif in indices and indices[dif] != i:
                return [i, indices[dif]]    