from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        states = [0] * numCourses

        def dfs(node):
            if states[node] == 1:
                return False
            if states[node] == 2:
                return True

            states[node] = 1

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            states[node] = 2
            return True

        for i in range(numCourses):
            if states[i] == 0:
                if not dfs(i):
                    return False

        return True


if __name__ == "__main__":
    sol = Solution()

    # тест 1
    num1 = 2
    prereq1 = [[1, 0]]
    res1 = sol.canFinish(num1, prereq1)
    print(f"тест 1: {str(res1).lower()} (ожидается: true)")

    # тест 2
    num2 = 2
    prereq2 = [[1, 0], [0, 1]]
    res2 = sol.canFinish(num2, prereq2)
    print(f"тест 2: {str(res2).lower()} (ожидается: false)")