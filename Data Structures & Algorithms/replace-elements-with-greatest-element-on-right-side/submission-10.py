class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        r_num = - 1
        res = [0] * len(arr)

        for i in range(len(arr)-1, -1,-1):
            
            res[i] = r_num
            r_num = max(r_num, arr[i])
        return res

        