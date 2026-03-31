from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: sort
        
        for i in range(len(nums)):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two-pointer search
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1  # need bigger sum
                elif total > 0:
                    r -= 1  # need smaller sum
                else:
                    # found triplet
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # skip duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res
