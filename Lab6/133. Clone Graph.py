from typing import Optional
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        cloned = {}

        def dfs(curr_node):
            if curr_node in cloned:
                return cloned[curr_node]

            copy = Node(curr_node.val)
            cloned[curr_node] = copy

            for neighbor in curr_node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)


# функция для построения графа из списка смежности
def build_graph(adj_list):
    if not adj_list:
        return None

    # создаем все узлы
    nodes = {i: Node(i) for i in range(1, len(adj_list) + 1)}

    # связываем узлы
    for i, neighbors in enumerate(adj_list):
        node = nodes[i + 1]
        for n_val in neighbors:
            node.neighbors.append(nodes[n_val])

    return nodes[1]


# функция для перевода графа обратно в список смежности для вывода
def graph_to_adj_list(node):
    if not node:
        return []

    visited = {}
    queue = deque([node])
    visited[node.val] = node

    # обходим граф через bfs
    while queue:
        curr = queue.popleft()
        for n in curr.neighbors:
            if n.val not in visited:
                visited[n.val] = n
                queue.append(n)

    res = []
    # формируем ответ согласно индексам
    for i in range(1, len(visited) + 1):
        res.append([n.val for n in visited[i].neighbors])

    return res


if __name__ == "__main__":
    sol = Solution()

    # тест 1
    adj1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    root1 = build_graph(adj1)
    res1 = sol.cloneGraph(root1)
    print(f"тест 1: {graph_to_adj_list(res1)} (ожидается: [[2, 4], [1, 3], [2, 4], [1, 3]])")

    # тест 2
    adj2 = [[]]
    root2 = build_graph(adj2)
    res2 = sol.cloneGraph(root2)
    print(f"тест 2: {graph_to_adj_list(res2)} (ожидается: [[]])")

    # тест 3
    adj3 = []
    root3 = build_graph(adj3)
    res3 = sol.cloneGraph(root3)
    print(f"тест 3: {graph_to_adj_list(res3)} (ожидается: [])")