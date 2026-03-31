class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        res = 0
        for ch in charSet:
            left = lenght = 0
            for i in range(len(s)):
                if s[i] == ch:
                    lenght += 1

            
                while (i - left + 1) - lenght > k:
                    if s[left] == ch:
                        lenght -= 1
                    left += 1
                
                res = max(res, i - left + 1)

        return res