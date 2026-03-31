class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        def dfs(sr, sc):
            if sr < 0:
                return
            if sc < 0:
                return

            if sr >= len(grid):
                return
            if sc >= len(grid[0]):
                return

            if grid[sr][sc] == '0':
                return 

            grid[sr][sc] = '0'

            for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(sr - r, sc - c)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1

                    dfs(i, j)

        return ans