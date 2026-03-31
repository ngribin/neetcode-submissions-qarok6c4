class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        h = set()
        res = 0

        for i in range(len(s)):
            while s[i] in h:
                h.remove(s[left])
                left += 1

            h.add(s[i])

            res = max(res, i - left + 1)
        return res
        