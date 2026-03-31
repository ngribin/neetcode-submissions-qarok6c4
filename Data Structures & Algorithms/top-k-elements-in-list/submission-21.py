class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_h = {}
        for num in nums:
            dict_h[num] = dict_h.get(num,0) + 1

        arr = []

        for num, cnt in dict_h.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res