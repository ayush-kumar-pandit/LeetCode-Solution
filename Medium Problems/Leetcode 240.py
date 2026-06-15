class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0]) - 1
        for rows in matrix:
            if rows[0] <= target <= rows[-1]:
                low, high = 0, n
                while low <= high:
                    mid = low + (high - low) // 2
                    if rows[mid] == target:
                        return True
                    elif rows[mid] < target:
                        low = mid + 1
                    else:
                        high = mid - 1
        return False