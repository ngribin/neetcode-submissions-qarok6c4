class Solution:
    def scoreOfString(self, s: str) -> int:
        sum_d = 0
        for i in range(1, len(s)):
            sum_d += abs(ord(s[i]) - ord(s[i-1]))

        return sum_d
        