class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                last_idx = stack[-1] if stack else - 1
                width = i - last_idx - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area
        