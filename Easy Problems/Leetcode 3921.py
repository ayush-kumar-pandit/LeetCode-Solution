class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        res = [0,0]
        for ch in events:
            if ch.isdigit():
                res[0] += int(ch)
            elif ch == "W":
                res[1] += 1
                if res[1] == 10:
                    return res
            else:
                res[0] += 1
        return res
