class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = [st for st in s.lower() if st.isalnum()]
        return st == st[::-1]