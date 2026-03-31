class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        h = {}
        for i, num in enumerate(nums):
            h[num] =  1 + h.get(num, 0)
        
        arr = []
        for num, cnt in h.items():
            arr.append([cnt, num])

        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])    
        return res    