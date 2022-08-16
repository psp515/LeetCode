class Solution(object):
    def count(self, s):
        arr = [0 for _ in range(26)]
        
        for letter in s:
            arr[ord(letter) - 97]+=1
        
        return arr
    
    def minSteps(self, s, t):
        count = 0
        
        tc = self.count(t)
        st = self.count(s)
        
        for i in range(26):
            count += abs(tc[i]-st[i])
            
        return count // 2
        