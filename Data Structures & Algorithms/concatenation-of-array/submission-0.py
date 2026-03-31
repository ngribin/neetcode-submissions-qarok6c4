class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums) * 2
        ans = [None] * n
        for i, num in enumerate(nums):
            ans[i] = num
            ans[i+len(nums)] = num
           



        return ans
        