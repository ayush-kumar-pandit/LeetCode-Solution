class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for ch in address:
            if ch != '.':
                res += ch
            else:
                res += "[.]"
        return res