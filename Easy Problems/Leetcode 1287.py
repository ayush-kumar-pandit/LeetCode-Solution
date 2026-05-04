class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return arr[0]
        sz = len(arr) // 4
        freq = {}
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        maxx = max(freq.values())
        for i in arr:
            if freq[i] == maxx:
                return i