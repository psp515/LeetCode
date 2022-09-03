class Solution(object):
    def minDistance(self, word1, word2):
        n, m = len(word1), len(word2)
        # f[i][j] - minimal dist if word to i-th index and j - th index 
        f = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(n + 1):
            f[i][0] = i
        for j in range(m + 1):
            f[0][j] = j
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i-1] == word2[j-1]:
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = 1 + min(f[i-1][j], f[i][j-1], f[i-1][j-1])
        
        return f[-1][-1]
                
        