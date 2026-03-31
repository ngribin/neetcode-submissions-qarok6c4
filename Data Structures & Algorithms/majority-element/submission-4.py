class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {

        }

        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        return max(count, key=count.get)