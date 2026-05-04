class Solution:
    def partitionString(self, s: str) -> int:
        st = ""
        res = []

        for ch in s:
            if ch not in st:
                st += ch
            else:
                res.append(st)
                st = ch
        return len(res) + 1