class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k  # Массив фиксированного размера
        self.capacity = k  # Максимальная вместимость
        self.size = 0  # Текущее количество элементов
        self.front = 0  # Индекс первого элемента
        self.rear = -1  # Индекс последнего элемента

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        # Перемещаем rear на следующую позицию (циклически)
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        # Перемещаем front на следующую позицию (циклически)
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

    def __str__(self) -> str:
        """Для удобного отображения состояния очереди"""
        if self.isEmpty():
            return "Queue: [] (empty)"

        # Собираем элементы в порядке очереди
        elements = []
        idx = self.front
        for _ in range(self.size):
            elements.append(self.queue[idx])
            idx = (idx + 1) % self.capacity

        return f"Queue: {elements}, array: {self.queue}, front={self.front}, rear={self.rear}, size={self.size}"


# Тестовые примеры
if __name__ == "__main__":
    print("=" * 70)
    print("Example 1 из условия задачи")
    print("=" * 70)

    myCircularQueue = MyCircularQueue(3)
    print(f"MyCircularQueue(3) → {myCircularQueue}")

    result = myCircularQueue.enQueue(1)
    print(f"enQueue(1) → {result}, {myCircularQueue}")

    result = myCircularQueue.enQueue(2)
    print(f"enQueue(2) → {result}, {myCircularQueue}")

    result = myCircularQueue.enQueue(3)
    print(f"enQueue(3) → {result}, {myCircularQueue}")

    result = myCircularQueue.enQueue(4)
    print(f"enQueue(4) → {result} (очередь полна!)")

    result = myCircularQueue.Rear()
    print(f"Rear()     → {result}")

    result = myCircularQueue.isFull()
    print(f"isFull()   → {result}")

    result = myCircularQueue.deQueue()
    print(f"deQueue()  → {result}, {myCircularQueue}")

    result = myCircularQueue.enQueue(4)
    print(f"enQueue(4) → {result}, {myCircularQueue}")

    result = myCircularQueue.Rear()
    print(f"Rear()     → {result}")

    print()
    print("=" * 70)
    print("Демонстрация циклического поведения")
    print("=" * 70)

    cq = MyCircularQueue(4)
    print(f"\nСоздана очередь размера 4: {cq}")

    print("\n--- Заполняем очередь ---")
    for i in range(1, 5):
        result = cq.enQueue(i * 10)
        print(f"enQueue({i * 10}) → {result}, {cq}")

    print("\n--- Удаляем 2 элемента ---")
    for _ in range(2):
        front_val = cq.Front()
        result = cq.deQueue()
        print(f"deQueue() (удалён {front_val}) → {result}, {cq}")

    print("\n--- Добавляем 2 новых элемента (циклический переход!) ---")
    for val in [50, 60]:
        result = cq.enQueue(val)
        print(f"enQueue({val}) → {result}, {cq}")

    print("\n--- Текущее состояние ---")
    print(f"Front() = {cq.Front()}")
    print(f"Rear()  = {cq.Rear()}")
    print(f"isEmpty() = {cq.isEmpty()}")
    print(f"isFull()  = {cq.isFull()}")

    print("\n--- Извлекаем все элементы ---")
    while not cq.isEmpty():
        front_val = cq.Front()
        cq.deQueue()
        print(f"Извлечён: {front_val}, {cq}")

    print("=" * 70)
    print("Тест граничных случаев")
    print("=" * 70)

    # Очередь размера 1
    print("\nОчередь размера 1:")
    q1 = MyCircularQueue(1)
    print(f"enQueue(100) → {q1.enQueue(100)}, {q1}")
    print(f"enQueue(200) → {q1.enQueue(200)} (полна!)")
    print(f"Front() = {q1.Front()}, Rear() = {q1.Rear()}")
    print(f"deQueue() → {q1.deQueue()}, {q1}")
    print(f"isEmpty() = {q1.isEmpty()}")
    print(f"Front() = {q1.Front()}, Rear() = {q1.Rear()}")