from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):
            if (r < 0 or r >= m or c < 0 or c >= n or
                    (r, c) in visited or heights[r][c] < prev_height):
                return

            visited.add((r, c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(n):
            dfs(0, c, pacific, heights[0][c])
            dfs(m - 1, c, atlantic, heights[m - 1][c])

        for r in range(m):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, n - 1, atlantic, heights[r][n - 1])

        return [[r, c] for r, c in pacific.intersection(atlantic)]


if __name__ == "__main__":
    sol = Solution()

    # тест 1
    heights1 = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
    res1 = sol.pacificAtlantic(heights1)
    # сортируем для удобного сравнения
    res1.sort()
    expected1 = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    expected1.sort()
    print(f"тест 1: {res1} (ожидается: {expected1})")

    # тест 2
    heights2 = [[1]]
    res2 = sol.pacificAtlantic(heights2)
    print(f"тест 2: {res2} (ожидается: [[0, 0]])")