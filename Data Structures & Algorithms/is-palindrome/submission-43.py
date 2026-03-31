class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]

        l, r = 0, len(s) - 1

        while l <= r:
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() == s[r].lower():
                return True

            else:
                l += 1
                r -= 1        


        