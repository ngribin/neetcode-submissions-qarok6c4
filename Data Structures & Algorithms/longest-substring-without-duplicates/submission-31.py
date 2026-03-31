class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charSet = set()
        left = 0

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[left])
                left += 1
            res = max(res, i - left + 1)
            charSet.add(s[i])

        return res