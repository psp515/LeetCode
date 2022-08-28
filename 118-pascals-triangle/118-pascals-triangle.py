class Solution(object):
    def generate(self, n):
        if n == 1:
            return [[1]]
        rows = [[1],[1,1]]
        i = 2
        while i < n:
            rows.append([1])
            for j in range(1, len(rows[i-1])):
                rows[i].append((rows[i-1][j-1] + rows[i-1][j]))
            rows[i].append(1)
            i += 1
        
        return rows
        