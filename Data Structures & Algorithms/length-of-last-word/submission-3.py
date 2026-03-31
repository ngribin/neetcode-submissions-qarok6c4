class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        i, lenght = len(s) - 1, 0
        lenght = 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            i -= 1
            lenght += 1 
        return lenght      
        