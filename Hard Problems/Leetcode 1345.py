class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 2:
            return n - 1
        if arr[0] == arr[-1]:
            return 1
        
        idx_map = defaultdict(list)
        for i,v in enumerate(arr):
            idx_map[v].append(i)
        
        visited = set()
        queue = deque([0])
        step = 0

        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                if i == n - 1:
                    return step
                
                next_step = idx_map[arr[i]] + [i + 1, i - 1]

                for x in next_step:
                    if x not in visited and x >= 0 and x <= n - 1:
                        visited.add(x)
                        queue.append(x)
                
                idx_map[arr[i]].clear()
            step += 1
        