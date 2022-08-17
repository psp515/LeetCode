class Solution(object):
    def validIndex(self, i, n):
        if -1 < i < n:
            return True
        return False

    def validIndexes(self, i, j, n, m):
        return self.validIndex(i, n) and self.validIndex(j, m)

    def islandExplore(self, grid, i, j, visited, n, m):

        visited[i][j] = True
        if self.validIndexes(i - 1, j, n, m) and visited[i - 1][j] == False and grid[i- 1][j] == '1':
            self.islandExplore(grid, i - 1, j, visited, n, m)

        if self.validIndexes(i + 1, j, n, m) and visited[i + 1][j] == False and grid[i+1][j] == '1':
            self.islandExplore(grid, i + 1, j, visited, n, m)

        if self.validIndexes(i, j - 1, n, m) and visited[i][j-1] == False and grid[i][j- 1] == '1':
            self.islandExplore(grid, i, j - 1, visited, n, m)

        if self.validIndexes(i, j + 1, n, m) and visited[i][j+1] == False and grid[i][j+1] == '1':
            self.islandExplore(grid, i, j + 1, visited, n, m)



    def numIslands(self, grid):
        n, m = len(grid), len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        count = 0

        for i in range(n):
            for j in range(m):
                if visited[i][j] == False:
                    if grid[i][j] == '1':
                        self.islandExplore(grid, i, j, visited, n, m)
                        count += 1
                    visited[i][j] = True

        return count