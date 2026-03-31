class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        h = defaultdict(int)
        count = 0
        for num in nums:
            count += h[num]
            h[num] += 1



            
        return count