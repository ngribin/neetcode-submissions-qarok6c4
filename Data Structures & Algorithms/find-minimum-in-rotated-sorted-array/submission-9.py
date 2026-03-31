class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # Initialize with first element or positive infinity
        min_number = nums[0]  # or float("inf")
        
        while left <= right:
            mid = (left + right) // 2
            
            # Update minimum
            min_number = min(min_number, nums[mid])
            
            # Check which side is sorted and contains the minimum
            if nums[mid] > nums[right]:
                # Left side is sorted, minimum might be in right side
                left = mid + 1
            else:
                # Right side is sorted, minimum might be in left side
                right = mid - 1
        
        return min_number