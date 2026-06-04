from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []

        for x in nums:
            i = bisect.bisect_left(sub, x)
            if i == len(sub):
                sub.append(x)
            else:
                sub[i] = x

        return len(sub)


if __name__ == "__main__":
    sol = Solution()

    # тест 1
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    res1 = sol.lengthOfLIS(nums1)
    print(f"тест 1: {res1} (ожидается: 4)")

    # тест 2
    nums2 = [0, 1, 0, 3, 2, 3]
    res2 = sol.lengthOfLIS(nums2)
    print(f"тест 2: {res2} (ожидается: 4)")

    # тест 3
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    res3 = sol.lengthOfLIS(nums3)
    print(f"тест 3: {res3} (ожидается: 1)")