class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = []
        if k == 0:
            return [0] * n
        elif k > 0:
            for i in range(n):
                j = i + 1
                x = 0
                while j <= i + k:
                    x += code[j % n]
                    j += 1
                res.append(x)
        else:
            for i in range(n):
                j = i - 1
                x = 0
                while j >= i + k:
                    x += code[j % n]
                    j -= 1
                res.append(x)
        return res