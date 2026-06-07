class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            rows = set()
            cols = set()
            for j in range(n):
                if matrix[i][j] in rows:
                    return False
                rows.add(matrix[i][j])
                
                if matrix[j][i] in cols:
                    return False
                cols.add(matrix[j][i])
        return True