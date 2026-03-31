class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_s = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in num_s:    
                lenght = 1

                while num + lenght in num_s:
                    lenght += 1

                longest = max(longest, lenght)

        return longest