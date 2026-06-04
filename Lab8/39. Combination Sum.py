from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, current_sum, path):
            if current_sum == target:
                res.append(path[:])
                return

            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, current_sum + candidates[i], path)
                path.pop()

        backtrack(0, 0, [])
        return res


if __name__ == "__main__":
    sol = Solution()

    # тест 1
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    res1 = sol.combinationSum(candidates1, target1)
    print(f"тест 1: {res1}")
    # ожидается любой порядок внутри, например: [[2, 2, 3], [7]]

    # тест 2
    candidates2 = [2, 3, 5]
    target2 = 8
    res2 = sol.combinationSum(candidates2, target2)
    print(f"тест 2: {res2}")
    # ожидается: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    # тест 3
    candidates3 = [2]
    target3 = 1
    res3 = sol.combinationSum(candidates3, target3)
    print(f"тест 3: {res3}")
    # ожидается: []