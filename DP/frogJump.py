class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        visited_set = set()
        stack = [(0, 0)]
        while stack:
            stone, jump = stack.pop()
            for j in [jump-1, jump, jump+1]:
                s = stone + j
                if (j > 0 and s in stone_set and (s, j) not in visited_set):
                    if (s == stones[-1]):
                        return True
                    stack.append((s, j))
            visited_set.add((stone, jump))
        return False
