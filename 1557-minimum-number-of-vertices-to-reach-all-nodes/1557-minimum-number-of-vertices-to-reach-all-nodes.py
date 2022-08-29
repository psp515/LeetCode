class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        f = [0 for _ in range(n)]
        
        for x in edges:
            f[x[1]] += 1
        ret = []
        for i in range(n):
            if f[i] == 0:
                ret.append(i)
        return ret
        
        