class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        res = 0
        
        rows = Counter()
        for v in grid:
            rows[tuple(v)] += 1   
        
        for i in range(len(grid[0])):
            ls = []
            for g in grid:
                ls.append(g[i])
            
            res += rows[tuple(ls)]   

        return res