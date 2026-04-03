class MyQueue:

    def __init__(self):
        self.stack_in = []  # Стек для добавления элементов
        self.stack_out = []  # Стек для извлечения элементов

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self._move_to_out()
        return self.stack_out.pop()

    def peek(self) -> int:
        self._move_to_out()
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out

    def _move_to_out(self) -> None:
        """Перемещаем элементы из stack_in в stack_out, если stack_out пуст"""
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

    def __str__(self) -> str:
        """Для удобного отображения состояния очереди"""
        # Элементы в порядке очереди: сначала stack_out (в обратном), потом stack_in
        queue_order = self.stack_out[::-1] + self.stack_in
        return f"Queue: {queue_order}, stack_in: {self.stack_in}, stack_out: {self.stack_out}"


# Тестовые примеры
if __name__ == "__main__":
    print("=" * 60)
    print("Example 1 из условия задачи")
    print("=" * 60)

    myQueue = MyQueue()
    print(f"MyQueue() → {myQueue}")

    myQueue.push(1)
    print(f"push(1)   → {myQueue}")

    myQueue.push(2)
    print(f"push(2)   → {myQueue}")

    result = myQueue.peek()
    print(f"peek()    → {result}, {myQueue}")

    result = myQueue.pop()
    print(f"pop()     → {result}, {myQueue}")

    result = myQueue.empty()
    print(f"empty()   → {result}")

    print()
    print("=" * 60)
    print("Дополнительные тесты")
    print("=" * 60)

    queue = MyQueue()
    print(f"\nСоздана пустая очередь: {queue}")
    print(f"empty() = {queue.empty()}")

    print("\n--- Добавляем элементы 1, 2, 3, 4, 5 ---")
    for i in range(1, 6):
        queue.push(i)
        print(f"push({i}) → {queue}")

    print("\n--- Извлекаем 2 элемента ---")
    for _ in range(2):
        val = queue.pop()
        print(f"pop() = {val} → {queue}")

    print("\n--- Добавляем ещё 6, 7 ---")
    queue.push(6)
    print(f"push(6) → {queue}")
    queue.push(7)
    print(f"push(7) → {queue}")

    print("\n--- Смотрим на первый элемент ---")
    print(f"peek() = {queue.peek()}")

    print("\n--- Извлекаем все оставшиеся элементы ---")
    while not queue.empty():
        val = queue.pop()
        print(f"pop() = {val} → {queue}")

    print(f"\nempty() = {queue.empty()}")

    print()
    print("=" * 60)
    print("Визуализация работы двух стеков")
    print("=" * 60)
