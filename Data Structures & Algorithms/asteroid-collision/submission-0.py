class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0

        while i < len(asteroids) - 1:
            left = asteroids[i]
            right = asteroids[i + 1]

            # есть столкновение
            if left > 0 and right < 0:
                if abs(left) > abs(right):
                    del asteroids[i + 1]
                elif abs(left) < abs(right):
                    del asteroids[i]
                else:
                    del asteroids[i:i + 2]

                if i > 0:
                    i -= 1
            else:
                i += 1

        return asteroids