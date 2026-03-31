class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            l, r = i+1, len(numbers) - 1
            temp = target - numbers[i]

            while l <=r:
                mid = (l+ r) // 2
                if numbers[mid] == temp:
                    return [i+1, mid + 1]

                elif numbers[mid]  <= temp:
                    l +=1

                else: 
                    r -= 1
        return []                   
        