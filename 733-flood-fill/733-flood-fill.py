class Solution(object):
    
    def validIndex(self, i, n):
        if -1 < i < n:
            return True
        return False
    
    def validIndexes(self, i,j, n,m):
        return self.validIndex(i, n) and self.validIndex(j, m)
    
    def floodFill(self, image, sr, sc, color):
        if color == image[sr][sc]:
            return image
        n,m = len(image), len(image[0])
        stack = [(sr,sc)]
        visited = [[False for _ in range(m)] for _ in range(n)]
        starting_color = image[sr][sc]
        while stack:
            a, b = stack.pop()
            if visited[a][b] == False:
                if image[a][b] == starting_color:
                    image[a][b] = color
                    
                    if self.validIndexes(a-1, b, n, m):
                        stack.append((a-1,b))
                        
                    if self.validIndexes(a+1, b, n, m):
                        stack.append((a+1,b))
                        
                    if self.validIndexes(a, b-1, n, m):
                        stack.append((a,b-1))
                        
                    if self.validIndexes(a, b+1, n, m):
                        stack.append((a,b+1))
        return image
        