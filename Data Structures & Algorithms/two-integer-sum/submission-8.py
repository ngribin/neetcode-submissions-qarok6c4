class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_idx = {}

        for idx, num in enumerate(nums):
            res_idx[num] = idx

        for idx, num in enumerate(nums):
            dif = target - num
            if dif in res_idx and res_idx[dif] != idx:
                return [idx, res_idx[dif]]   
        