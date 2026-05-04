class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        copy = [row[:] for row in matrix]
        
        for i in range(len(copy)):
            k = 0
            for j in range(len(copy) - 1, -1, -1):
                matrix[i][k] = copy[j][i]
                k += 1
        