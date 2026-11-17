class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        if k == 1:
            return min(sum(map(ne, s, ''.join(s[i - d:i] for i in range(n, 0, -d)))) // 2 for d in range(1, n) if n % d == 0)

        top = n - 2 * (k - 1)  
        mismatches = [list(accumulate(map(ne, s, s[shift:]), initial=0)) for shift in range(top)]  
        cost = [[inf] * (n - length + 1) for length in range(top + 1)]  
        for d in range(1, top // 2 + 1):
            for first in (2 * d, 3 * d):  
                peeled = [0] * (n + 1)
                for length in range(first, top + 1, 2 * d):  
                    starts = n - length + 1
                    p = mismatches[length - d]  
                    outer = map(sub, p[d:d + starts], p[:starts])  
                    peeled = list(map(add, outer, peeled[d:d + starts]))  
                    cost[length] = list(map(min, cost[length], peeled))  

        best, cuts = [0] + [inf] * n, range(1)  
        for pieces in range(1, k):  
            room = range(2 * pieces, n - 2 * (k - pieces) + 1)
            new = [inf] * (n + 1)
            for length in range(2, top + 1):
                i = slice(cuts.start, min(cuts.stop, room.stop - length))
                j = slice(i.start + length, i.stop + length)  
                new[j] = map(min, new[j], map(add, best[i], cost[length][i]))
            best, cuts = new, room
        return min(best[i] + cost[n - i][i] for i in cuts)  