from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = '0'

            while queue:
                row, col = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        queue.append((nr, nc))
                        grid[nr][nc] = '0'

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i, j)

        return count


if __name__ == "__main__":
    sol = Solution()

    # тест 1
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    res1 = sol.numIslands(grid1)
    print(f"тест 1: {res1} (ожидается: 1)")

    # тест 2
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    res2 = sol.numIslands(grid2)
    print(f"тест 2: {res2} (ожидается: 3)")