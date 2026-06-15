class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outerLow = 0
        outerHigh = len(matrix) - 1
        while outerLow <= outerHigh:
            outerMid = outerLow + (outerHigh - outerLow) // 2
            if matrix[outerMid][0] <= target <= matrix[outerMid][-1]:
                innerLow = 0
                innerHigh = len(matrix[0]) - 1
                while innerLow <= innerHigh:
                    innerMid = innerLow + (innerHigh - innerLow) // 2
                    if matrix[outerMid][innerMid] == target:
                        return True
                    elif matrix[outerMid][innerMid] > target:
                        innerHigh = innerMid - 1
                    else:
                        innerLow = innerMid + 1
                else:
                    return False
            elif matrix[outerMid][0] > target:
                outerHigh = outerMid - 1
            else:
                outerLow = outerMid + 1
        return False