class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #find all unique
        #find the start of seq
        #go + 1 in order to find end

        num_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in num_set:
                lenght = 1

                while num+ lenght in num_set:
                    lenght += 1

                longest = max(longest, lenght)

        return longest 
        