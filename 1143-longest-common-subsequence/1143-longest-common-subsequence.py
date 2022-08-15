class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        n, m = len(text1), len(text2)
        f = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                tmp = 0
                if text1[i-1] == text2[j-1]:
                    tmp = f[i-1][j-1] + 1
                f[i][j] = max(tmp, f[i-1][j], f[i][j-1])
                                            
        return f[-1][-1]
                
        