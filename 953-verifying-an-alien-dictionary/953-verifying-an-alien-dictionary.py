class Solution(object):
    def twosorted(self, prev, next, d): 
        for i in range(min(len(prev), len(next))):
            if d[prev[i]] < d[next[i]]:
                return True
            elif d[prev[i]] == d[next[i]]:
                continue
            else:
                return False
                 
        return len(prev) <= len(next)
        
    def isAlienSorted(self, words, order):
        d = {}    
        i = 0
        for letter in order:
            d[letter] = i
            i += 1
        
        for i in range(1, len(words)):
            if not self.twosorted(words[i-1], words[i], d):
                return False
        
        return True