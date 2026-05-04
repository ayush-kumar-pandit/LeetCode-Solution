class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if target == mat:
            return True
        for i in range(len(mat) + 1):
            copy = [row[:] for row in mat]
            
            for i in range(len(copy)):
                k = 0
                for j in range(len(copy) - 1, -1, -1):
                    copy[i][k] = mat[j][i]
                    k += 1
            
            if copy == target:
                return True
            mat = [row[:] for row in copy]
        return False