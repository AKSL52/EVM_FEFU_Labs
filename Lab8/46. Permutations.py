from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res


if __name__ == "__main__":
    sol = Solution()

    # тест 1
    nums1 = [1, 2, 3]
    res1 = sol.permute(nums1)
    print(f"тест 1: {res1}")
    # ожидается любой порядок, например: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

    # тест 2
    nums2 = [0, 1]
    res2 = sol.permute(nums2)
    print(f"тест 2: {res2}")
    # ожидается: [[0, 1], [1, 0]]

    # тест 3
    nums3 = [1]
    res3 = sol.permute(nums3)
    print(f"тест 3: {res3}")
    # ожидается: [[1]]