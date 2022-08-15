class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        act, prev = 1, 0
        i = 1
        while i < n:
            i += 1
            act, prev = act + prev , act
        
        return act
        
        
        