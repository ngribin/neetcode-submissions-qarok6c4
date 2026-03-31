class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                heightIdx = stack[-1] if stack else -1
                width = i - heightIdx - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area
        