class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        water = 0

        while left < right:
            if height[left] <= height[right]:
                left += 1
                max_left = max(max_left, height[left])
                water += max_left - height[left]


            else:
                right -= 1
                max_right = max(height[right], max_right)
                water += max_right - height[right]
        return water

        