class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        hash_map_dict = {}

        for i, num in enumerate(nums):
            hash_map_dict[num] = hash_map_dict.get(num, 0) + 1

        arr = []

        for num, cnt in hash_map_dict.items():
            arr.append([cnt, num])

        arr.sort()

        res = []
        while len(res) < k:
            res_ = arr.pop()[1]
            res.append(res_)
        return res              
            