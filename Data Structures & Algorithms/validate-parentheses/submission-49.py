class Solution:
    def isValid(self, s: str) -> bool:
        h = {
            "}":"{",
            ")":"(",
            "]":"[",
        }

        stack = []

        for ch in s:
            if ch in h.values():
                stack.append(ch)

            elif ch in h:
                if not stack:
                    return False

                if stack[-1] != h[ch]:
                    return False

                stack.pop()
        return len(stack) == 0 