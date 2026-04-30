class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        for i,v in enumerate(arr):
            if v not in d:
                d[v] = i
        temp = []
        for i in d.keys():
            temp.append(i)
        temp.sort()
        res = []

        d2 = {}
        for i,v in enumerate(temp):
            if v not in d2:
                d2[v] = i
        for i in arr:
            res.append(d2[i] + 1)
        return res
