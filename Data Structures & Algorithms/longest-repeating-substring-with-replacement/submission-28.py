class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for ch in s:
            left = count = 0
            for i in range(len(s)):
                if ch == s[i]:
                    count += 1

                while (i - left + 1) - count > k:
                    if ch == s[left]:
                        count -= 1
                    left += 1

                res = max(res, i - left + 1)

        return res 
