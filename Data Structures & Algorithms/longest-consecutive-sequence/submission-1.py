class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for i, num in enumerate(nums):
            if num - 1 not in num_set:
                lenght = 1
                while num + lenght in num_set:
                    lenght += 1

                longest = max(longest, lenght)
        return longest