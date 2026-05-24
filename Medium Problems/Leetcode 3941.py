class Solution:
    def passwordStrength(self, password: str) -> int:
        score = 0
        seen = set()
        for ch in password:
            if ch not in seen and ch.isdigit():
                seen.add(ch)
                score += 3
            elif ch not in seen and ch in "!@#$":
                seen.add(ch)
                score += 5
            elif ch not in seen and ch.islower():
                seen.add(ch)
                score += 1
            elif ch not in seen:
                seen.add(ch)
                score += 2

        return score