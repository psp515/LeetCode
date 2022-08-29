class Solution(object):
    def findJudge(self, n, trust):
        
        if n == 1:
            return 1 if trust == [] else -1 
        
        tc = [0 for _ in range(n + 1)]
        ta = [0 for _ in range(n + 1)]
        for x,y in trust:
            tc[y] += 1
            ta[x] = True
            
        judges = 0
        j_i = -1
        for i in range(n + 1):
            if tc[i] == n - 1 and not ta[i]:
                judges += 1
                j_i = i
        
        return -1 if judges != 1 else j_i
                
        