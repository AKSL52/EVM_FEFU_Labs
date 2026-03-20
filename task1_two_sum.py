from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    # 1. Создаем объект нашего класса
    my_solution = Solution()

    # 2. Берем тестовые данные из примера на LeetCode (Example 1)
    test_nums = [2, 7, 11, 15]
    test_target = 9

    # 3. Вызываем функцию и сохраняем то, что она "вернула" (return), в переменную result
    result = my_solution.twoSum(test_nums, test_target)

    # 4. Печатаем результат на экран
    print("Ответ:", result)
