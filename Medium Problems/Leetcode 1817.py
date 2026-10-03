class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        hashmap = defaultdict(set)

        for user, minute in logs:
            hashmap[user].add(minute)

        res = [0] * k

        for minutes in hashmap.values():
            uam = len(minutes)
            res[uam - 1] += 1

        return res
