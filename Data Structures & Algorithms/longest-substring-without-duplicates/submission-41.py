class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = set()
        left = 0
        res = 0
        for i in range(len(s)):
            while s[i] in h:
                h.remove(s[left])
                left += 1
            res = max(res, i - left + 1)
            h.add(s[i])
            
        return res