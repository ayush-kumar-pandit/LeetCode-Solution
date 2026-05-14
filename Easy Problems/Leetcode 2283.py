class Solution:
    def digitCount(self, num: str) -> bool:
        d = {}
        for ch in num:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        for i in range(len(num)):
            if str(i) in d and int(num[i]) != d[str(i)]:
                return False
            elif num[i] != '0' and str(i) not in d:
                return False

        return True