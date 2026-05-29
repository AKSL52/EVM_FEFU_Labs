from collections import deque


# структура узла бинарного дерева
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root


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


# функция для поиска узла по значению (нужна для передачи p и q)
def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    if val < root.val:
        return find_node(root.left, val)
    return find_node(root.right, val)


if __name__ == "__main__":
    sol = Solution()

    # тест 1
    root1 = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p1 = find_node(root1, 2)
    q1 = find_node(root1, 8)
    res1 = sol.lowestCommonAncestor(root1, p1, q1)
    print(f"тест 1: {res1.val if res1 else None} (ожидается: 6)")

    # тест 2
    root2 = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p2 = find_node(root2, 2)
    q2 = find_node(root2, 4)
    res2 = sol.lowestCommonAncestor(root2, p2, q2)
    print(f"тест 2: {res2.val if res2 else None} (ожидается: 2)")

    # тест 3
    root3 = build_tree([2, 1])
    p3 = find_node(root3, 2)
    q3 = find_node(root3, 1)
    res3 = sol.lowestCommonAncestor(root3, p3, q3)
    print(f"тест 3: {res3.val if res3 else None} (ожидается: 2)")