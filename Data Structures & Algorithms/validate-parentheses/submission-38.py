class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        
        stack = []
        for ch in s:
            if ch in hashmap.values():
                stack.append(ch)

            elif ch in hashmap:
                if not stack:
                    return False
                if stack[-1] != hashmap[ch]:

                    return False
                stack.pop()
        return len(stack) == 0