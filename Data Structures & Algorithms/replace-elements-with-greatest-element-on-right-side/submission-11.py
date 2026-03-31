class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1] * len(arr)

        rM = - 1

        for i in range(len(arr) - 1, -1, -1):
            ans[i] = rM
            rM = max(rM, arr[i])

        return ans

