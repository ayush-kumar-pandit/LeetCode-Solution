class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) == 1:
            return False
        flag = False
        for i in range(len(arr) - 1):
            if not flag:
                if arr[i] >= arr[i + 1]:
                    if i == 0 or arr[i] == arr[i + 1]:
                        return False
                    flag = True
                
            else:
                if arr[i] < arr[i + 1] or arr[i] == arr[i - 1]:
                    return False
        return flag