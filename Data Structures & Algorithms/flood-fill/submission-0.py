
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]

        if start_color == color:
            return image

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return

            if image[r][c] != start_color:
                return

            image[r][c] = color

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc)

        dfs(sr, sc)
        return image