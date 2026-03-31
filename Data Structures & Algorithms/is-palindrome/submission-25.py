class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [st for st in s.lower() if st.isalnum()]
        return s == list(reversed(s))           
        