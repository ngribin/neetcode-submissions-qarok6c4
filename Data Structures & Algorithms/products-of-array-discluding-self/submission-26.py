class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res_forword = []

        prod = 1
        for num in nums:
            res_forword.append(prod)
            prod *= num

        backward_res = []
        prod = 1
        for num in nums[::-1]:
            backward_res.append(prod)
            prod *= num

        res = []
        for a, b in zip(res_forword,backward_res[::-1]):
            res.append(a * b)

        return res