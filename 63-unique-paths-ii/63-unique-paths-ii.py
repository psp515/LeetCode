class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        if n == 1 and m == 1:
            return (obstacleGrid[0][0] + 1) % 2

        if obstacleGrid[0][0]:
            return 0

        # f[i][j] - number of paths to [i][j] field
        f = [[0 for _ in range(m)] for _ in range(n)]

        f[0][0] = 1

        for i in range(1, n):
            if obstacleGrid[i][0] == 0 and f[i-1][0] != 0:
                f[i][0] = 1

        for j in range(1, m):
            if obstacleGrid[0][j] == 0 and f[0][j-1] != 0:
                f[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 0:
                    f[i][j] = f[i - 1][j] + f[i][j - 1]

        return f[-1][-1]