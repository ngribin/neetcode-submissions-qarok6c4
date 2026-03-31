class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [(p, s) for p, s in zip(position, speed)]

        for p, s in sorted(pairs):
            time = (target - p) / s

            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)

        return len(stack)        
        