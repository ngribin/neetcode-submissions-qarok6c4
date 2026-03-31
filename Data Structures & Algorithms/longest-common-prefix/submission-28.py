class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    
        res = strs[0]
    
        for i in range(1, len(strs)):
            left = 0
            while left < min(len(strs[i]), len(res)):
                if strs[i][left] != res[left]:
                    break
                left += 1
            res = res[:left]

        return res
