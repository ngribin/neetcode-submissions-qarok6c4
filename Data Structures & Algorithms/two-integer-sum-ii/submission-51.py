class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left, right = 0, len(numbers) - 1

            while left <= right:
                mid = (left + right) // 2
                diff = target - numbers[i]
                if numbers[mid] == diff:
                    return [i+1, mid+1]
                elif numbers[mid] < diff:
                    left += 1

                else:
                    right -= 1
        