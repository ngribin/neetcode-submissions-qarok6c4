class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        n = len(temperatures)
        res = [0] * n

        for i, num in enumerate(temperatures):
            while stack and stack[-1][1] < num:
                tempIdx, tempS = stack.pop()
                res[tempIdx] = i - tempIdx 
            stack.append((i, num))

        return res 
        