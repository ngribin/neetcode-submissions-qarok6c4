class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left, right = 0, len(numbers) - 1
            while left <= right:
                mid = (left+right ) // 2
                if numbers[mid] == target-numbers[i]:
                    return [i+1, mid+1]
                elif numbers[mid] <= target-numbers[i]:
                    left = mid + 1
                else:
                    right = mid - 1
        return []            
# for range
# temp
# while -> mid -> temp? mid + 1 -1