class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        G = [[[], []] for i in xrange(n)]
        
        for i, j in redEdges: 
            G[i][0].append(j)
        for i, j in blueEdges: 
            G[i][1].append(j)
            
        res = [[0, 0]] + [[n * 2, n * 2] for i in xrange(n - 1)]
        stack = [[0, 0], [0, 1]]
        
        for i, c in stack:
            for j in G[i][c]:
                if res[j][c] == n * 2:
                    res[j][c] = res[i][1 - c] + 1
                    stack.append([j, 1 - c])
                    
        return [x if x < n * 2 else -1 for x in map(min, res)]
        
        