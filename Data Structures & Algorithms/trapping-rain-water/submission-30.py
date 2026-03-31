class Solution:
    def trap(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        max_left, max_right = height[left], height[right]

        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(height[left], max_left)
                max_area += max_left - height[left]

            else:
                right -= 1
                max_right = max(height[right], max_right)
                max_area += max_right - height[right]

        return max_area 

        