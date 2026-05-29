from typing import Optional, List
from collections import deque


# структура узла бинарного дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(current_level)

        return res


# функция для построения дерева из списка (bfs)
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


if __name__ == "__main__":
    sol = Solution()

    # тест 1
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    res1 = sol.levelOrder(root1)
    print(f"тест 1: {res1} (ожидается: [[3], [9, 20], [15, 7]])")

    # тест 2
    root2 = build_tree([1])
    res2 = sol.levelOrder(root2)
    print(f"тест 2: {res2} (ожидается: [[1]])")

    # тест 3
    root3 = build_tree([])
    res3 = sol.levelOrder(root3)
    print(f"тест 3: {res3} (ожидается: [])")