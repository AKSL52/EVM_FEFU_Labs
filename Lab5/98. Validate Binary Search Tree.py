from typing import Optional
from collections import deque


# структура узла бинарного дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root)


# функция для построения дерева из списка
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
    root1 = build_tree([2, 1, 3])
    res1 = sol.isValidBST(root1)
    print(f"тест 1: {res1} (ожидается: true)")

    # тест 2
    root2 = build_tree([5, 1, 4, None, None, 3, 6])
    res2 = sol.isValidBST(root2)
    print(f"тест 2: {res2} (ожидается: false)")