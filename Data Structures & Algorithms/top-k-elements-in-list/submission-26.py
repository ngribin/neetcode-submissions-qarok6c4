class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result_dict = {}
        for num in nums:
            result_dict[num] = result_dict.get(num,0) + 1

        list_of_count = [(cnt, num) for num, cnt in result_dict.items()]
        # for num, cnt in result_dict.items():    
        #     list_of_count.append([cnt, num])
        list_of_count.sort()
        results = []
        while len(results) < k:
            results.append(list_of_count.pop()[1]) 
        return results      

        