class Solution(object):
    def dfsVisit(self, G, u, visited, routes):
        visited[u] = True

        for i in G[u]:
            if visited[i] == False:
                routes[(i, u)] = True
                self.dfsVisit(G, i, visited, routes)
    
    def graphify(self, routes, n):
        G=[[] for _ in range(n)]
        
        for i,j in routes:
            G[i].append(j)
            G[j].append(i)
        
        return G
        
    def minReorder(self, n, connections):
        G = self.graphify(connections, n)
        visited = [False for _ in range(n)]
        
        routes = {}
        
        self.dfsVisit(G, 0, visited, routes)
        
        counter = 0
        
        for a,b in connections:
            if (a, b) in routes:
                continue
            else:
                counter += 1
        
        return counter
        
        