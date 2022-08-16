class Solution(object):
    def areOccurrencesEqual(self, s):
        if len(s) == 0:
            return True
        
        counter = [0 for _ in range(26)]
        
        for letter in s:
            counter[ord(letter)-97] += 1
        
        cmp = counter[ord(s[0])-97]
        
        for i in range(len(counter)):
            if counter[i] != 0 and counter[i] != cmp:
                return False
        return True