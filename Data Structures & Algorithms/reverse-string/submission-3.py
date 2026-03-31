class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []

        for ch in s:
            stack.append(ch)

        index = 0
        while stack:
            s[index] = stack.pop()
            index += 1