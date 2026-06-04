from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res


if __name__ == "__main__":
    sol = Solution()

    # тест 1
    nums1 = [1, 2, 3]
    res1 = sol.subsets(nums1)
    print(f"тест 1: {res1}")
    # ожидается порядок любой, например: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

    # тест 2
    nums2 = [0]
    res2 = sol.subsets(nums2)
    print(f"тест 2: {res2}")
    # ожидается: [[], [0]]