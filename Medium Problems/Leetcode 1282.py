class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        d = defaultdict(list)
        for i, val in enumerate(groupSizes):
            if val == 1:
                ans.append([i])
            else:
                d[val].append(i)
                if len(d[val]) == val:
                    ans.append(d[val])
                    d[val] = []

        return ans 