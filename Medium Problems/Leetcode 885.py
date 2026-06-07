class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        step = 0
        res.append([rStart,cStart])
        d = 0
        while len(res) != cols * rows:
            if d == 0 or d == 2:
                step += 1
            for i in range(step):
                rStart += directions[d][0]
                cStart += directions[d][1]

                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
            d = (d + 1) % 4
        return res