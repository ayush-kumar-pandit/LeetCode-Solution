class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lengths = [0] * (n + 1)
        for i, ch in enumerate(s):
            if ch.islower():
                lengths[i + 1] = lengths[i] + 1
            elif ch == '*':
                lengths[i + 1] = max(0, lengths[i] - 1)
            elif ch == '#':
                lengths[i + 1] = min(10**15, lengths[i] * 2)
            else:  
                lengths[i + 1] = lengths[i]

        if k >= lengths[n]:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]

            if ch.islower():
                if k == lengths[i]:
                    return ch

            elif ch == '#':
                prev_len = lengths[i]
                k %= prev_len

            elif ch == '%':
                k = lengths[i] - 1 - k

        return '.'