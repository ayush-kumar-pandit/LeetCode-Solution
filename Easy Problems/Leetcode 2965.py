class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = set()
        n = len(grid) * len(grid)
        ls = [i for i in range(1, n + 1)]
        missing = 0
        repeat = 0
        for row in grid:
            for i in row:
                if i in s:
                    repeat = i
                s.add(i)
        for i in ls:
            if i not in s:
                missing = i
        return [repeat, missing]