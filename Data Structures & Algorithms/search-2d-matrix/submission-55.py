class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        r, c = 0, cols - 1

        while r < rows and c >= 0:
            val = matrix[r][c]
            if target == val:
                return True

            if target < val:
                c -= 1

            else:
                r += 1
        return False