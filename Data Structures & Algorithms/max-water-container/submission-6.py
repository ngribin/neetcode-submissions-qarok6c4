class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        end = len(heights) - 1
        max_area = 0

        while left <= end:
            current_area = min(heights[left], heights[end]) * (end-left)
            max_area = max(current_area, max_area)

            if heights[left] <= heights[end]:
                left += 1
            else:
                end -= 1
        return max_area            