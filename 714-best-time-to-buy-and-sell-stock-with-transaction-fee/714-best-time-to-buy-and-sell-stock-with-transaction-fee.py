class Solution(object):
    def maxProfit(self, arr, fee):
        # O(n^2)
        #n = len(arr)
        # f[i] - max income to i-th day
        #f = [0 for _ in range(n)]
        #for i in range(1, n):
        #    for j in range(i-1, -1, -1):
        #        if arr[i]- arr[j] - fee > 0:
        #            f[i] = max(f[i], f[j] + arr[i] - arr[j] - fee)
        #        f[i] = max(f[i], f[i-1])
        # return f[-1]
        
        n = len(arr)
        # f[i][state] - maximum income to -i-th day
        # state = 1 - seeling stock
        # state = 0 - buying this stock
        f = [[0, 0] for _ in range(n+1)]
        
        for i in range(n-1,-1,-1):
            # buying 
            f[i][0] = max(f[i+1][0], f[i+1][1] - arr[i])
            # selling
            f[i][1] = max(f[i+1][1], f[i+1][0] + arr[i] - fee)
        
        return f[0][0]
    
    
    

        
        
        