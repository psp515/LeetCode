

class Solution(object):
    def dfsVisit(self, G, i, visited, n):
        visited[i] = True
        
        for u in G[i]:
            if not visited[u]: 
                self.dfsVisit(G, u, visited,n)
        
    def findNotConected(self, G):
        n = len(G)
        count = 0
        visited = [False for _ in range(n)]
        
        for i in range(n):
            if not visited[i]:
                self.dfsVisit(G, i, visited,n)
                count += 1
        
        return count 
    
    def graphify(self, n, routes):
        G =[[] for _ in range(n)]
        
        for x,y in routes:
            G[x].append(y)
            G[y].append(x)
        
        return G
    
    def makeConnected(self, n, routes):
        cables = len(routes)
        
        if cables + 1 < n:
            return -1
        
        G = self.graphify(n, routes)
        
        return self.findNotConected(G) - 1 
        