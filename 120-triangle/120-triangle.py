class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)

        if n == 1:
            return triangle[0][0]

        f = [[float('inf') for _ in range(i + 1)] for i in range(n + 1)]
        f[0][0] = 0
        for i in range(n):
            for j in range(i + 1):
                f[i + 1][j] = min(f[i + 1][j], f[i][j] + triangle[i][j])
                f[i + 1][j + 1] = min(f[i + 1][j + 1], f[i][j] + triangle[i][j])

        return min(f[-1])
        