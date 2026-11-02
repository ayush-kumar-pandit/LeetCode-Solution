class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        ls = []
        for row in grid:
            for i in row:
                ls.append(i)
        ls.sort()
        res = 0
        target = ls[len(ls) // 2]
        for i in ls:
            diff = abs(target - i)
            if diff % x:
                return -1
            res += diff // x
        return res