class Solution(object):
    def deleteAndEarn(self, nums):
        
        d = {}
        
        for num in nums:
            if num in d:
                d[num] +=1
            else:
                d[num] = 1 
        
        # f[i] - max income till i-th element
        g = list(d.items())
        g.sort(key = lambda x : x[0])
        n = len(g)
        
        if n == 1:
            return g[0][1]*g[0][0]
        
        if n == 2:
            if g[0][0] + 1 == g[1][0]:
                return max(g[0][0] * g[0][1], g[1][0] * g[1][1])
            return g[1][0] * g[1][1] + g[0][0] * g[0][1]
        
        f = [0 for _ in range(n)]
        f[0] = g[0][0] * g[0][1]
        
        if g[0][0] + 1 == g[1][0]:
            f[1] = max(f[0], g[1][0] * g[1][1])
        else:
            f[1] = g[1][0] * g[1][1] + g[0][0] * g[0][1]
        
        
        for i in range(2, n):
            if g[i][0] - 1 == g[i-1][0]:
                f[i] = max(f[i-1], g[i][0] * g[i][1] + f[i-2])
            else:
                f[i] = f[i-1] + g[i][0] * g[i][1]
        
        return f[-1]