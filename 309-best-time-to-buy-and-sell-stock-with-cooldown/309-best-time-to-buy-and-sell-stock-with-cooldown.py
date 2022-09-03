class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        
        if n < 2:
            return 0
        
        # f[i][state] - max profit to i-th day with state
        # 0 - cooldown
        # 1 - buying this stock 
        # 2 - selling this stock
        f = [[0, 0, 0] for _ in range(n)]
        f[0][0] = 0
        f[0][1] = -prices[0]
        f[0][2] = -float('inf')
        
        max_buy = f[0][1]
        
        for i in range(1, n):
            f[i][0] = max(f[i-1][0], f[i-1][1], f[i-1][2])
            f[i][1] = f[i-1][0] - prices[i]
            f[i][2] = max_buy + prices[i]
            
            max_buy = max(max_buy, f[i][1])
        
        return max(f[-1][0], f[-1][2])
    
        