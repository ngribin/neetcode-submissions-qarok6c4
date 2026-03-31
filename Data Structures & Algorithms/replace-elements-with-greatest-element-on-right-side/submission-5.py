class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        max_right = -1

        for i in range(len(arr)-1,-1,-1):
            res[i] = max_right
            max_right = max(arr[i], max_right)
        
        return res