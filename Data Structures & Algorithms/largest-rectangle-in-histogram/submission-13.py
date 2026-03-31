class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights.append(0)

        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                heidhIdx = stack[-1] if stack else -1
                width = i - heidhIdx - 1
                max_area = max(max_area, width * h)
            stack.append(i)
        return max_area