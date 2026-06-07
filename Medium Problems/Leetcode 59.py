class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        r = n
        l = 0
        u = 0
        d = n 
        res = [[0] * n for _ in range(n)]
        i = 1
        while l < r and u < d:
            for j in range(l,r):
                res[u][j] = i
                i += 1
            u += 1
            for j in range(u,d):
                res[j][r - 1] = i
                i += 1
            r -= 1
            if not (l < r and u < d):
                break
            for j in range(r - 1,l - 1, -1):
                res[d - 1][j] = i
                i += 1
            d -= 1
            for j in range(d - 1,u - 1, -1):
                res[j][l] = i
                i += 1
            l += 1
        return res

