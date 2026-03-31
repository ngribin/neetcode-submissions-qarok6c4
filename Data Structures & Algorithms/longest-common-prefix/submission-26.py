class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        

        for i in range(1, len(strs)):
            left = 0
            while left < min(len(prefix), len(strs[i])):
                if prefix[left] != strs[i][left]:
                    break
                left += 1    


            prefix = prefix[:left]
        return prefix
        