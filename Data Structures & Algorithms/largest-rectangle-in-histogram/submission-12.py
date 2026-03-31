class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []          # indices of increasing heights
        max_area = 0
        heights.append(0)   # sentinel to flush stack

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left_smaller_idx = stack[-1] if stack else -1
                width = i - left_smaller_idx - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        heights.pop()       # optional cleanup
        return max_area