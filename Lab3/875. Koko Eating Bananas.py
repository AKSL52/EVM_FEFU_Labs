class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k

            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.minEatingSpeed([3, 6, 7, 11], 8))       # 4
    print(sol.minEatingSpeed([30, 11, 23, 4, 20], 5)) # 30
    print(sol.minEatingSpeed([30, 11, 23, 4, 20], 6)) # 23