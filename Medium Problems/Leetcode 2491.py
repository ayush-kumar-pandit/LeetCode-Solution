class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        i, j = 1, len(skill) - 2
        s = skill[0] + skill[-1]
        res = skill[0] * skill[-1]
        while i < j:
            if skill[i] + skill[j] != s:
                return -1
            res += skill[i] * skill[j]
            i += 1
            j -= 1
        return res