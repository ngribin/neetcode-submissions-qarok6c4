class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [1] * n
        

        
        product_left = 1
        for i in range(n):
            res[i] *= product_left
            product_left *= nums[i]

        product_right = 1
        for i in range(n - 1, - 1, -1):
            res[i] *= product_right
            product_right *= nums[i]          

        return res