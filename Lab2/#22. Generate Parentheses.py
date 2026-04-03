def generateParenthesis(n: int) -> list[str]:
    result = []

    def backtrack(current: str, open_count: int, close_count: int):
        # Базовый случай: собрали строку нужной длины
        if len(current) == 2 * n:
            result.append(current)
            return

        # Можем добавить '(' если ещё не использовали все
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        # Можем добавить ')' если есть незакрытые '('
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    backtrack('', 0, 0)
    return result


# Тестовые примеры
if __name__ == "__main__":
    # Example 1
    n1 = 3
    print(f"Input: n = {n1}")
    print(f"Output: {generateParenthesis(n1)}")
    print()

    # Example 2
    n2 = 1
    print(f"Input: n = {n2}")
    print(f"Output: {generateParenthesis(n2)}")
    print()

    # Дополнительные тесты
    n3 = 2
    print(f"Input: n = {n3}")
    print(f"Output: {generateParenthesis(n3)}")
    print()

    n4 = 4
    print(f"Input: n = {n4}")
    print(f"Output: {generateParenthesis(n4)}")
    print(f"Количество комбинаций: {len(generateParenthesis(n4))}")
    print()

    # Визуализация процесса для n = 2
    print("=" * 50)
    print("Визуализация процесса для n = 2:")
    print("=" * 50)


    def generateWithTrace(n: int):
        result = []

        def backtrack(current: str, open_count: int, close_count: int, depth: int):
            indent = "  " * depth
            print(f"{indent}Вызов: current='{current}', open={open_count}, close={close_count}")

            if len(current) == 2 * n:
                print(f"{indent}✅ Найдено: '{current}'")
                result.append(current)
                return

            if open_count < n:
                print(f"{indent}→ Добавляем '('")
                backtrack(current + '(', open_count + 1, close_count, depth + 1)

            if close_count < open_count:
                print(f"{indent}→ Добавляем ')'")
                backtrack(current + ')', open_count, close_count + 1, depth + 1)

            print(f"{indent}← Возврат")

        backtrack('', 0, 0, 0)
        return result


    result = generateWithTrace(2)
    print()
    print(f"Итоговый результат для n=2: {result}")