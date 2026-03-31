class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for char in charSet:
            left = count = 0

            for i in range(len(s)):
                if s[i] == char:
                    count += 1

                while (i - left + 1) - count > k:
                    if s[left] == char:
                        count -= 1
                    left += 1

                res = max(res, i - left + 1)
        return res 

        