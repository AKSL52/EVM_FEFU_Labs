from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0

        for n in nums:
            temp = max(n + prev2, prev1)
            prev2 = prev1
            prev1 = temp

        return prev1


if __name__ == "__main__":
    sol = Solution()

    # тест 1
    nums1 = [1, 2, 3, 1]
    res1 = sol.rob(nums1)
    print(f"тест 1: {res1} (ожидается: 4)")

    # тест 2
    nums2 = [2, 7, 9, 3, 1]
    res2 = sol.rob(nums2)
    print(f"тест 2: {res2} (ожидается: 12)")