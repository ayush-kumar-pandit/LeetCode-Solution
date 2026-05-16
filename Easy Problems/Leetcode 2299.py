class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        lower = False
        upper = False
        digit = False
        special = False
        spcl_char = "!@#$%^&*()-+"
        prev = ""
        for ch in password:
            if ch == prev:
                return False
            if ch.isdigit():
                digit = True
            elif ch in spcl_char:
                special = True
            elif ch.isupper():
                upper = True
            elif ch.islower():
                lower = True
            prev = ch
        return lower and upper and digit and special