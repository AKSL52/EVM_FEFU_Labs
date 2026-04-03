def evalRPN(tokens: list[str]) -> int:
    stack = []

    for token in tokens:
        if token in {'+', '-', '*', '/'}:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            else:  # token == '/'
                result = int(a / b)

            stack.append(result)
        else:
            stack.append(int(token))

    return stack[0]


# Тестовые примеры
if __name__ == "__main__":
    # Example 1
    tokens1 = ["2", "1", "+", "3", "*"]
    print(f"Input: tokens = {tokens1}")
    print(f"Output: {evalRPN(tokens1)}")
    print(f"Explanation: ((2 + 1) * 3) = 9")
    print()

    # Example 2
    tokens2 = ["4", "13", "5", "/", "+"]
    print(f"Input: tokens = {tokens2}")
    print(f"Output: {evalRPN(tokens2)}")
    print(f"Explanation: (4 + (13 / 5)) = 6")
    print()

    # Example 3
    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(f"Input: tokens = {tokens3}")
    print(f"Output: {evalRPN(tokens3)}")
    print(f"Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22")
    print()

    # Дополнительные тесты
    tokens4 = ["3", "4", "+"]
    print(f"Input: tokens = {tokens4}")
    print(f"Output: {evalRPN(tokens4)}")
    print()

    tokens5 = ["10", "6", "9", "3", "+", "-11", "*", "/"]
    print(f"Input: tokens = {tokens5}")
    print(f"Output: {evalRPN(tokens5)}")
    print()

    # Тест с отрицательным делением
    tokens6 = ["-7", "2", "/"]
    print(f"Input: tokens = {tokens6}")
    print(f"Output: {evalRPN(tokens6)}")
    print(f"Explanation: -7 / 2 = -3 (truncate toward zero)")
    print()