class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = set()
        left = 0
     
        for i, num in enumerate(nums):
            while (i - left) > k:
                h.remove(nums[left])
                left += 1

            
            if num in h:
                return True
            h.add(num)
        return False