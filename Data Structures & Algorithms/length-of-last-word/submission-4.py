class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l_w = [word for word in s.split()]
        return len(l_w[-1])
        