class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                temp_idx, stackT = stack.pop()
                result[temp_idx] = i - temp_idx
            stack.append((i, temp))
        return result

        