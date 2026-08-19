from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = defaultdict(list)

        for row, seat in reservedSeats:
            rows[row].append(seat)

        ans = (n - len(rows)) * 2

        for seats in rows.values():
            seats.sort()

            left = all(seat not in seats for seat in range(2, 6))

            middle = all(seat not in seats for seat in range(4, 8))

            right = all(seat not in seats for seat in range(6, 10))

            if left and right:
                ans += 2

            elif left or middle or right:
                ans += 1

        return ans
