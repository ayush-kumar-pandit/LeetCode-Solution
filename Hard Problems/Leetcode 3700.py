class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        def mat_mul(A, B):
            n1, n2, n3 = len(A), len(B), len(B[0])
            C = [[0] * n3 for _ in range(n1)]

            for i in range(n1):
                for k in range(n2):
                    if A[i][k] == 0:
                        continue
                    aik = A[i][k]
                    for j in range(n3):
                        C[i][j] = (C[i][j] + aik * B[k][j]) % MOD
            return C

        def mat_pow(A, p):
            n = len(A)
            R = [[0] * n for _ in range(n)]
            for i in range(n):
                R[i][i] = 1

            while p:
                if p & 1:
                    R = mat_mul(R, A)
                A = mat_mul(A, A)
                p >>= 1
            return R

        steps = n - 1

        U = [[0] * m for _ in range(m)]
        D = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(i):
                U[i][j] = 1
            for j in range(i + 1, m):
                D[i][j] = 1

        UD = mat_mul(U, D)

        V = mat_pow(UD, steps // 2)

        if steps & 1:
            V = mat_mul(V, U)

        ans = 0
        for row in V:
            ans = (ans + sum(row)) % MOD

        return (ans * 2) % MOD