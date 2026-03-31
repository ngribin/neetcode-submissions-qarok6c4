class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                idx = stack[-1] if stack else - 1
                witdh = i - idx - 1
                max_area = max(max_area, height * witdh)
            stack.append(i)

        return max_area
