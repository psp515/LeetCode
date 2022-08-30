class Solution(object):
    def rank(self, G, i, j):
        r = len(G[i]) + len(G[j])
        
        for x in G[i]:
            if x == j:
                r -= 1
                break
        
        return r
        
        
        
    def maximalNetworkRank(self, n, roads):
        G = [[] for _ in range(n)]
        
        for rs,re in roads:
            G[rs].append(re)
            G[re].append(rs)
        maxr = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                maxr = max(maxr, self.rank(G, i, j))
        
        return maxr
                