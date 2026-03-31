class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = set()
        left = 0

        for i, num in enumerate(nums):
            if i - left > k:
                h.remove(nums[left])
                left += 1
            if nums[i] in h:
                return True

            h.add(nums[i])

        return False
        