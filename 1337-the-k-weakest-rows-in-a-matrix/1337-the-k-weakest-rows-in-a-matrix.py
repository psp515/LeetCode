class Solution(object):
    def kWeakestRows(self, mat, k):
        n = len(mat)
        f = [(sum(mat[i]), i) for i in range(n)]  
        f.sort(key = lambda x:x[1])
        f.sort(key = lambda x:x[0])
        f = [f[i][1] for i in range(n)]
        return f[:k]
        