class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        n = len(digits) - 1
        add = digits[-1] + 1
        carry = 0
        while (add > 9 or carry) and n >= 0:
            digits[n] = add % 10
            carry = add // 10
            n -= 1
            add = carry + digits[n]
        if carry:
            digits.reverse()
            digits.append(1)
            digits.reverse()
        return digits