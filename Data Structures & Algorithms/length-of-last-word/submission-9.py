class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = lenght = 0
        while i < len(s):
            if s[i] == " ":
                while i < len(s) and s[i] == ' ':
                    i += 1
                if i == len(s):
                    return lenght

                lenght = 0
            else:
                lenght += 1
                i += 1
                

        return lenght
        