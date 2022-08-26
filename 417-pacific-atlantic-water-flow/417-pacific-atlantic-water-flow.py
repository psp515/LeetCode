class Solution(object):
    def bfs(self, map , stack, heights):
        n, m = len(heights), len(heights[0])
        
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        for x, y in stack:
            visited[x][y] = True

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        while stack:
            x, y = stack.popleft()
            
            
            
            for x1, y1 in dirs:
                nx, ny = x + x1, y + y1
                if 0 <= nx < n and 0 <= ny < m and heights[nx][ny] >= heights[x][y] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    map[nx][ny] = True
                    stack.append([nx, ny])
    
    def pacificAtlantic(self, heights):
        n,m = len(heights), len(heights[0])
        
        pmap = [[False for _ in range(m)] for _ in range(n)]
        amap = [[False for _ in range(m)] for _ in range(n)]
        
        stack = deque([(i,0) for i in range(n)] + [(0,i) for i in range(m)])
        for x,y in stack:
            pmap[x][y] = True
        self.bfs(pmap, stack, heights)
        
        stack = deque([(i,m-1) for i in range(n)] + [(n-1, i) for i in range(m)])
        for x,y in stack:
            amap[x][y] = True
        self.bfs(amap, stack, heights)
        
        returnable = []
        
        for i in range(n):
            for j in range(m):
                if pmap[i][j] and amap[i][j]:
                    returnable.append([i, j])    
                    
        return returnable 
        
        
        
        
        