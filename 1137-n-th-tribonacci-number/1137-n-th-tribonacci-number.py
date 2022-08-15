class Solution(object):
    def tribonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        act, prev, prevprev = 1, 1, 0
        i = 2
        while i < n:
            i+=1
            act, prev, prevprev = act + prev + prevprev, act, prev
            
        return act