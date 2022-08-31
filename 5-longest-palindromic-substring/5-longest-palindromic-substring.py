class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        f = [[False for _ in range(n)] for _ in range(n)]
        
        sequnece = ''
        for i in range(n):
            f[i][i] = True
            
        sequnece = s[0]
    
        
        for i in range(n-1,-1,-1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j-i == 1 or f[i+1][j-1] is True:
                        f[i][j] = True
                        ns = s[i:j+1]
                        if len(sequnece) < len(ns):
                            sequnece = ns
            
        
        return sequnece
                        
        


