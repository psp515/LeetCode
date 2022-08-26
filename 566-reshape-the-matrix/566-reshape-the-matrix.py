class Solution(object):
    def matrixReshape(self, mat, r, c):
        n, m = len(mat), len(mat[0])
        
        if r*c != n * m:
            return mat
        
        linear = []
        
        for i in range(n):
            for j in range(m):
                linear.append(mat[i][j])
        
        returnable = [[-1 for _ in range(c)] for _ in range(r)]
        
        k = 0
        for i in range(r):
            for j in range(c):
                returnable[i][j] = linear[k]
                k += 1
                
        return returnable
        