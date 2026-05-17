class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def DFS(arr: List[int], i: int) -> bool:
            if i < 0 or i >= len(arr) or arr[i] == -1:
                return False
            if arr[i] == 0:
                return True
            
            x = arr[i] 
            arr[i] = -1 
            
            left = DFS(arr,i - x)
            right = DFS(arr, i + x)
            return left or right
        return DFS(arr,start)
