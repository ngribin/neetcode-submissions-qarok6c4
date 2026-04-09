class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right = - 1
        res = [0] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            res[i] = right
            right = max(arr[i], right)

        return res
        