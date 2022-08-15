class Solution(object):
    def maximumWealth(self, accounts):
        n = len(accounts)
        # f[i] - biggest wealth from all objects from 0 to i
        f = [0 for _ in range(n)]
        f[0] = sum(accounts[0])
        for i in range(1, n):
            f[i] = max(f[i-1], sum(accounts[i]))
        
        return f[-1]
        
        
        
        