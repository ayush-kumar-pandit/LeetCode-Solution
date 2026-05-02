class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0

        for g in grid:
            g.sort(reverse = True)

        for i in range(len(grid[0])):
            ls = []
            for g in grid:
                ls.append(g[i])
            res += max(ls)
        return res 
