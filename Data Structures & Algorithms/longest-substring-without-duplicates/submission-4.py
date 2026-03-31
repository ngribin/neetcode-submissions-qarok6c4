class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = result = 0
        seen = {}

        for idx, letter in enumerate(s):
            if seen.get(letter, -1) >= start:
                start = seen[letter] + 1
            result = max(result, idx - start + 1)
            seen[letter] = idx
        return result