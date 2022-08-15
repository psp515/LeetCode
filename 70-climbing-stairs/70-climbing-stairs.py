class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        
        # f[i] - liczba sposobów wejswcia na i-ty schód
        f = [float('inf') for _ in range(n)]
        f[0] = 1
        f[1] = 2
        for i in range(2, n):
            f[i] = f[i-1] + f[i-2]
        
        return f[-1]
        
        