class Solution(object):
    def change(self, amount, coins):
        f = [0 for _ in range(amount+1)]
        f[0] = 1
        
        for coin in coins:
            for i in range(amount+1):
                if coin <= i:
                    f[i] += f[i-coin]
                    
        return f[-1] 