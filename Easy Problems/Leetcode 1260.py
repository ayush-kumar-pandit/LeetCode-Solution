class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ls = []
        for row in grid:
            for i in row:
                ls.append(i)
        k = k % len(ls)
        ls.reverse()
        new1 = ls[:k]
        new1.reverse()
        new2 = ls[k:]
        new2.reverse()
        ls = new1 + new2
        n = len(grid)
        m = len(grid[0])
        x = 0
        for i in range(n):
            for j in range(m):
                grid[i][j] = ls[x]
                x += 1
        return grid