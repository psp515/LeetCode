class Solution(object):
    def coinChange(self, coins, amount):
        f = [float('inf') for _ in range(amount+1)]
        f[0] = 0
        
        for i in range(amount+1):
            for coin in coins:
                if coin == i:
                    f[i] = 1
                elif coin < i:
                    f[i]= min(f[i],f[i-coin] + 1)
                    
        return f[-1] if f[-1] != float('inf') else -1
        