class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        x = len(original)
        if m * n != x:
            return []
        res = []
        i = 0
        while i < x:
            ls = []
            for j in range(i, i + n):
                ls.append(original[j])
            res.append(ls)
            i += n
        return res
