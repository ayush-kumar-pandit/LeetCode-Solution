class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count('Y')
        best_penalty = penalty
        answer = 0

        for hour, ch in enumerate(customers):
            if ch == 'Y':
                penalty -= 1
            else:
                penalty += 1

            if penalty < best_penalty:
                best_penalty = penalty
                answer = hour + 1

        return answer