class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for num in nums:
            h[num] = h.get(num, 0) + 1

        arr = []
        for key, val in h.items():
            arr.append((key, val))
        arr.sort(key=lambda x: x[1])

        res = []
        while len(res) < k:
            res.append(arr.pop()[0])
        return res

        