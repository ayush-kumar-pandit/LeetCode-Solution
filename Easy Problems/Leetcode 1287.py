class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        x = len(arr)
        y = x // 4
        for i in range(x - y):
            if arr[i] == arr[i + y]:
                return arr[i]