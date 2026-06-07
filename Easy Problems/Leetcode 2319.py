class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        j = len(grid) - 1
        diagonal = set()
        n = len(grid)
        for i in range(n):
            if not grid[i][i] or not grid[i][j]:
                return False
            diagonal.add((i,j))
            diagonal.add((i,i))

            j -= 1
        for i in range(n):
            for j in range(n):
                if (i,j) not in diagonal:
                    if grid[i][j]:
                        return False
        return True
        