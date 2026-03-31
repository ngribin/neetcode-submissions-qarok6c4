class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for num in nums:
            h[num] = h.get(num, 0) + 1

        arr = []
        for key, val in h.items():
            arr.append((val, key))
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        