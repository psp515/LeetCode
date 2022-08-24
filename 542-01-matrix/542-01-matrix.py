class Solution(object):
    def setup(self,grid, i, j):
        grid[i][j] = 0
        return i, j
    
    def updateMatrix(self, grid):
        n, m = len(grid), len(grid[0])
        
        dist = [[float('inf') for _ in range(m)] for _ in range(n)]
        stack = deque([self.setup(dist, i, j) for i in range(n) for j in range(m) if grid[i][j] == 0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        while stack:
            x, y = stack.popleft()
            for x1, y1 in dirs:
                nx, ny = x + x1, y + y1
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                    if dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        stack.append([nx, ny])
                    
        
        return dist
        