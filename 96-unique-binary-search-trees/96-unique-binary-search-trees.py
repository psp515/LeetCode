class Solution(object):
    def numTrees(self, n):
        
        f = [0 for _ in range(n+1)]
        
        f[0] = 1
        f[1] = 1
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                f[i] += f[j-1] * f[i-j] 
        
        return f[n]
            
        