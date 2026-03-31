class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        
        stack = []

        for char in s:
            if char in hashmap.values():
                stack.append(char)

            elif char in hashmap:
                if not stack:
                    return False
                elif hashmap[char] != stack[-1]:
                    return False

                stack.pop()

        return len(stack) == 0
