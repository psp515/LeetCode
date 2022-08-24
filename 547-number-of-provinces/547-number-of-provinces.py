class Solution(object):
    
    def dfsVisit(self, G, i, visited, n):
        visited[i] = True
        
        for u in range(n):
            if not visited[u] and G[i][u] == 1: 
                self.dfsVisit(G, u, visited,n)
        
    def findCircleNum(self, G):
        n = len(G)
        count = 0
        visited = [False for _ in range(n)]
        
        for i in range(n):
            if not visited[i]:
                self.dfsVisit(G, i, visited,n)
                count += 1
        
        return count        