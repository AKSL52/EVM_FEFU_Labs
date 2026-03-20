from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # ставим два указателя по краям
        left = 0
        right = len(height) - 1

        # переменная для хранения максимальной площади
        max_area = 0

        # идем навстречу друг другу, пока указатели не встретятся
        while left < right:
            # считаем текущую ширину
            current_width = right - left

            # высота ограничена самой короткой линией
            current_height = min(height[left], height[right])

            # считаем текущую площадь
            current_area = current_width * current_height

            # обновляем максимальную площадь, если текущая больше
            max_area = max(max_area, current_area)

            # сдвигаем тот указатель, чья линия короче
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    my_solution = Solution()

    # тестовые данные из примера 1
    test_height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    # вызываем функцию
    result = my_solution.maxArea(test_height)

    # печатаем результат. ожидаемый ответ: 49
    print(f"Максимальное количество воды: {result}")