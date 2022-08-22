class Solution(object):
    
    def letters(self, s1, s2):
        counter = [0 for _ in range(26)]
        
        for i in range(len(s1)):
            counter[ord(s1[i])-97] += 1
            counter[ord(s2[i])-97] -= 1
        
        for x in counter:
            if x != 0:
                return False
        
        return True
    
    def areAlmostEqual(self, s1, s2):
        if s1 == s2:
            return True
        
        counter = 0
        for i in range(len(s1)):
            if s1[i]!= s2[i]:
                counter += 1
        
        return counter == 2 and self.letters(s1, s2)
        
        