class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = []
        while k:
            n.append(k % 10)
            k //= 10
        n.reverse()
        i = len(num) - 1
        j = len(n) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            add = carry
            if i >= 0:
                add += num[i]
                i -= 1
            if j >= 0:
                add += n[j]
                j -= 1
            res.append(add % 10)
            carry = add // 10
        res.reverse()
        return res
        