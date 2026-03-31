class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        arr = []
        for num, cnt in seen.items():
            arr.append([cnt, num])

        arr.sort()

        result = []

        while len(result) < k:
            result.append(arr.pop()[1])   

        return result