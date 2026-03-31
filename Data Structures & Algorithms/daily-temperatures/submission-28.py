class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, tmpr in enumerate(temperatures):
            while stack and stack[-1][1] < tmpr:
                idx, temp = stack.pop()
                res[idx] = i - idx

            stack.append((i, tmpr))

        return res