from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == "__main__":
    sol = Solution()

    # тест 1
    coins1 = [1, 2, 5]
    amount1 = 11
    res1 = sol.coinChange(coins1, amount1)
    print(f"тест 1: {res1} (ожидается: 3)")

    # тест 2
    coins2 = [2]
    amount2 = 3
    res2 = sol.coinChange(coins2, amount2)
    print(f"тест 2: {res2} (ожидается: -1)")

    # тест 3
    coins3 = [1]
    amount3 = 0
    res3 = sol.coinChange(coins3, amount3)
    print(f"тест 3: {res3} (ожидается: 0)")