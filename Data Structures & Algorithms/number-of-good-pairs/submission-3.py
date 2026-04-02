class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        h = defaultdict(int)

        for num in nums:
            count += h[num]
            h[num] += 1

        return count