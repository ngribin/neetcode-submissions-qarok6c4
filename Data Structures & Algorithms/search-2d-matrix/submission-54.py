class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        row, col = 0, cols- 1

        while row < rows and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            
            if val > target:
                col -= 1

            else:
                row += 1

        return False