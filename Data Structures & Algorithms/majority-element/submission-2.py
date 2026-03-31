class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        for num in nums:
           
            h[num] = h.get(num, 0) + 1

        max_value = max(h, key=h.get)

        return max_value
        