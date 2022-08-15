class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        
        # f[i] - liczba sposobów wejswcia na i-ty schód
        act,prev = 2, 1
        for i in range(2, n):
            act,prev = act+ prev, act
        
        return act
        
        