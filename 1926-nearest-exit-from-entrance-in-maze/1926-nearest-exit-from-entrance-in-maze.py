class Solution(object):
    def nearestExit(self, maze, entrance):
        n, m = len(maze), len(maze[0])
        q = deque([entrance])
        a, b = entrance
        dist = [[float('inf') for _ in range(m)] for _ in range(n)]
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dist[a][b] = 0

        while q:
            x, y = q.popleft()

            if (x == n - 1 or y == m - 1 or y == 0 or x == 0) and (x != a or b != y):
                return dist[x][y]

            for x1, y1 in dirs:
                nx, ny = x + x1, y + y1
                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '.':
                    if dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append([nx, ny])

        return -1
        
        