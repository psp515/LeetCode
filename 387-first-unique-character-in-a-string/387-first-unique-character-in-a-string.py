class Solution(object):
    def firstUniqChar(self, s):
        n = len(s)
        counts = [0 for _ in range(26)]
        
        for letter in s:
            counts[ord(letter)-97] += 1
        
        for i in range(n):
            if counts[ord(s[i])-97] == 1:
                return i
        
        return -1
        