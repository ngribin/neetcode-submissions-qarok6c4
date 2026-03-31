class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = result = 0
        h = {}
        for idx, letter in enumerate(s):
            if h.get(letter, -1) >= start:
                start = h[letter] + 1
            result = max(idx - start+1, result)
            h[letter] = idx
        return result