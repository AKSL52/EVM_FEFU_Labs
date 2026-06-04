from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = '#'

            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            board[r][c] = temp
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False


if __name__ == "__main__":
    sol = Solution()

    # тест 1
    board1 = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word1 = "ABCCED"
    res1 = sol.exist(board1, word1)
    print(f"тест 1: {str(res1).lower()} (ожидается: true)")

    # тест 2
    board2 = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word2 = "SEE"
    res2 = sol.exist(board2, word2)
    print(f"тест 2: {str(res2).lower()} (ожидается: true)")

    # тест 3
    board3 = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word3 = "ABCB"
    res3 = sol.exist(board3, word3)
    print(f"тест 3: {str(res3).lower()} (ожидается: false)")