class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        if arr[0] != 1:
            arr[0] = 1
        n = len(arr)
        for i in range(n - 1):
            if arr[i] + 2 <= arr[i + 1]:
                arr[i + 1] = arr[i] + 1
        return arr[-1]