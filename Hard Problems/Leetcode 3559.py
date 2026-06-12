class Solution:
    def assignEdgeWeights(self, edges, queries):
        MOD = 10**9 + 7
        n = len(edges) + 1
        LOG = 17

        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        depth = [0] * (n + 1)
        up = [[-1] * (n + 1) for _ in range(LOG)]

        def dfs(u, p):
            up[0][u] = p
            for v in g[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    dfs(v, u)

        dfs(1, -1)

        for k in range(1, LOG):
            for v in range(1, n + 1):
                if up[k - 1][v] != -1:
                    up[k][v] = up[k - 1][up[k - 1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != -1 and depth[up[k][u]] >= depth[v]:
                    u = up[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return up[0][u]

        ans = []

        for u, v in queries:
            a = lca(u, v)
            d = depth[u] + depth[v] - 2 * depth[a]

            if d == 0:
                ans.append(0)
            else:
                ans.append(pow(2, d - 1, MOD))

        return ans