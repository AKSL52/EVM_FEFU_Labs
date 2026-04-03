def isValid(s: str) -> bool:
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}

    for c in s:
        if c in matching:
            if not stack or stack[-1] != matching[c]:
                return False
            stack.pop()
        else:
            stack.append(c)

    return not stack


# Тестовые примеры
if __name__ == "__main__":
    # Example 1
    s1 = "()"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {isValid(s1)}")
    print()

    # Example 2
    s2 = "()[]{}"
    print(f"Input: s = \"{s2}\"")
    print(f"Output: {isValid(s2)}")
    print()

    # Example 3
    s3 = "(]"
    print(f"Input: s = \"{s3}\"")
    print(f"Output: {isValid(s3)}")
    print()

    # Example 4
    s4 = "([])"
    print(f"Input: s = \"{s4}\"")
    print(f"Output: {isValid(s4)}")
    print()

    # Example 5
    s5 = "([)]"
    print(f"Input: s = \"{s5}\"")
    print(f"Output: {isValid(s5)}")
    print()

    # Дополнительные тесты
    s6 = "{[]}"
    print(f"Input: s = \"{s6}\"")
    print(f"Output: {isValid(s6)}")
    print()

    s7 = "((("
    print(f"Input: s = \"{s7}\"")
    print(f"Output: {isValid(s7)}")