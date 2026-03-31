class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        num_set = set(nums)
        for n in num_set:
            if n - 1 not in num_set: # found left bound where no number to start
                lenght = 1
                while n + lenght in num_set:
                    lenght += 1
                longest = max(longest, lenght)
        return longest
        