class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i, num in enumerate(asteroids):
            while stack and stack[-1] > 0 and num < 0:
                diff = num + stack[-1]
                if diff > 0:
                    num = 0
                elif diff < 0:
                    stack.pop()
                else:
                    stack.pop()
                    num = 0
            if num:
                stack.append(num)
        return stack