from typing import Optional
from collections import deque


# определение структуры узла бинарного дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# вспомогательная функция для построения дерева из списка
def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # левый потомок
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # правый потомок
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


if __name__ == "__main__":
    sol = Solution()

    # тест 1
    # входные данные: root = [3,9,20,null,null,15,7]
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    res1 = sol.maxDepth(root1)
    print(f"тест 1: {res1} (ожидается: 3)")

    # тест 2
    # входные данные: root = [1,null,2]
    root2 = build_tree([1, None, 2])
    res2 = sol.maxDepth(root2)
    print(f"тест 2: {res2} (ожидается: 2)")