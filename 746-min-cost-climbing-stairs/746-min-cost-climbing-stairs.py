class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        cost +=[0]
        # f[i] - minimal cost to get ot the i-th field 
        f = [float('inf') for _ in range(n+1)] 
        f[0] = cost[0]
        f[1] = cost[1]
        for i in range(2, n+1):
            f[i] = min(f[i-1], f[i-2]) + cost[i]
        
        return f[-1]
        
        