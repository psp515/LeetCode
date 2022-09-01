class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        f = [False for _ in range(n+1)]
        f[0] = True
        for i in range(n):
            for j in range(i, n):
                if f[i] and s[i: j+1] in wordDict:
                    f[j+1] = True
                    
        return f[-1]