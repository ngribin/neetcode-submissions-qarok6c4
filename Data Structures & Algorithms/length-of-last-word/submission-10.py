class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = count = 0
        while i < len(s):
            if s[i] == ' ':
                while i < len(s) and s[i] == " ":
                    i += 1
                if i == len(s):
                    return count

                count = 0
            
            else:
                count += 1
                i+= 1

        return count
        