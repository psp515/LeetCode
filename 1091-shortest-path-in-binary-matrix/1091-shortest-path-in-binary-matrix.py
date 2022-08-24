class Solution(object):
    def shortestPathBinaryMatrix(self, grid):

        if grid[-1][-1]:
            return -1

        n, m = len(grid), len(grid[0])
        stack = deque([(0, 0)])
        dist = [[float('inf') for _ in range(m)] for _ in range(n)]
        dist[0][0] = 1
        
        while stack:
            x, y = stack.popleft()

            if grid[x][y] == 1:
                continue

            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0:
                        continue
                    if 0 <= x + i < n and 0 <= y + j < m:
                        new_dist = dist[x][y] + 1
                        if new_dist < dist[x+i][y+j]:
                            dist[x + i][y + j] = new_dist
                            stack.append((x + i, y + j))

        return -1 if dist[-1][-1] == float('inf') else dist[-1][-1]