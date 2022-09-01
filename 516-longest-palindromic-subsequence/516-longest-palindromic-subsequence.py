class Solution(object):
    def isPalindrome(self, s1):
        return s == s[::-1]
    
    def longestPalindromeSubseq(self, s):
        t=s[::-1]  
        n = len(s)
        if t == s:
            return len(s)
        
        f = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        for i in range(1, n + 1):  
            for j in range(1, n + 1):
                if s[i-1]!=t[j-1]:  
                    f[i][j] = max(f[i][j-1], f[i-1][j]) 
                else:             
                    f[i][j] = 1 + f[i-1][j-1]  
                    
        return f[-1][-1]
        