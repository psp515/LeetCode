class Solution(object):
    def graph(self, n, array):
        g = [[] for _ in range(n)]

        for x, y in array:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)

        return g
    
    def dfsvisit(self, i, graph, visited):
        visited[i] = True
        
        for u in graph[i]:
            if not visited[u]:
                self.dfsvisit(u, graph, visited)
    
    def dfs(self, graph):
        n = len(graph)
        starts = []
        visited = [False for _ in range(n)]
        
        for i in range(n):
            if visited[i] == False:
                starts.append((i, 0))
                self.dfsvisit(i, graph, visited)
        
        return starts
    
    def isBipartite(self, graph):
        stack = self.dfs(graph)
        n = len(graph)
        # colors
        f = [-1 for _ in range(n)]
        f[0] = 0

        while stack:
            x, c = stack.pop()

            for y in graph[x]:
                if f[y] == -1:
                    if c == 1:
                        f[y] = 0
                        stack.append((y, 0))
                    else:
                        f[y] = 1
                        stack.append((y, 1))
                elif f[y] == 1:
                    if c == 1:
                        return False
                else:
                    if c == 0:
                        return False

        return True

    def possibleBipartition(self, n, dislikes):
        G = self.graph(n, dislikes)

        return self.isBipartite(G)
        