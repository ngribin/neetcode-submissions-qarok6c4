class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        window = set()

        for right in range(len(nums)):
            if right - left > k:
                window.remove(nums[left])
                left += 1
            if nums[right] in window:
            #if nums[left] == nums[right] and (right - left) <= k:
                return True
            window.add(nums[right])

        return False