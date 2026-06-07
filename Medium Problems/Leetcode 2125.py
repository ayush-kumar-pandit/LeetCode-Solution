class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        c1 = 0 
        c2 = 0
        for laser in bank:
            c1 = laser.count('1')
            res += c1 * c2
            if c1:
                c2 = c1
        return res   