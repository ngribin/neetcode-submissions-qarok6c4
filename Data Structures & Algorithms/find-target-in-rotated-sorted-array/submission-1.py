class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check which side is sorted
            if nums[left] <= nums[mid]:  # Left side is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is in left sorted portion
                else:
                    left = mid + 1  # Target is in right unsorted portion
            else:  # Right side is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Target is in right sorted portion
                else:
                    right = mid - 1  # Target is in left unsorted portion
        
        return -1
        