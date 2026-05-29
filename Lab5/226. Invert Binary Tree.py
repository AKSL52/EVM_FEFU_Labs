from typing import Optional
from collections import deque


# определение структуры узла бинарного дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# вспомогательная функция для построения дерева из массива
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# вспомогательная функция для перевода дерева обратно в массив для проверки
def tree_to_list(root):
    if not root:
        return []
    res = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    # очистка концевых none
    while res and res[-1] is None:
        res.pop()
    return res


if __name__ == "__main__":
    sol = Solution()

    # тест 1
    root1 = build_tree([4, 2, 7, 1, 3, 6, 9])
    res1 = sol.invertTree(root1)
    print(f"тест 1: {tree_to_list(res1)}")  # ожидается: [4, 7, 2, 9, 6, 3, 1]

    # тест 2
    root2 = build_tree([2, 1, 3])
    res2 = sol.invertTree(root2)
    print(f"тест 2: {tree_to_list(res2)}")  # ожидается: [2, 3, 1]

    # тест 3
    root3 = build_tree([])
    res3 = sol.invertTree(root3)
    print(f"тест 3: {tree_to_list(res3)}")  # ожидается: []