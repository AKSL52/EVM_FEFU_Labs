from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            # Ключ - отсортированная строка
            key = "".join(sorted(s))
            res[key].append(s)
        return list(res.values())

if __name__ == "__main__":
    sol = Solution()
    # Тест 1
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    # Тест 2
    print(sol.groupAnagrams([""]))
    # Тест 3
    print(sol.groupAnagrams(["a"]))