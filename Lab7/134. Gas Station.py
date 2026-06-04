from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        current_gas = 0
        start_index = 0

        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                current_gas = 0
                start_index = i + 1

        return start_index


if __name__ == "__main__":
    sol = Solution()

    # тест 1
    gas1 = [1, 2, 3, 4, 5]
    cost1 = [3, 4, 5, 1, 2]
    res1 = sol.canCompleteCircuit(gas1, cost1)
    print(f"тест 1: {res1} (ожидается: 3)")

    # тест 2
    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]
    res2 = sol.canCompleteCircuit(gas2, cost2)
    print(f"тест 2: {res2} (ожидается: -1)")