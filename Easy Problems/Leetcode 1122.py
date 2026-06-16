class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {}
        for i in arr1:
            freq[i] = freq.get(i, 0) + 1
        res = []
        for i in arr2:
            for j in range(freq[i]):
                res.append(i)
            del freq[i]
        temp = []
        s = set(arr2)
        for i in arr1:
            if i not in s:
                temp.append(i)
        temp.sort()
        return res + temp
    