class Solution(object):
    def repeatedCharacter(self, s):
        n = len(s)
        counts = [0 for _ in range(26)]
        
        for letter in s:
            counts[ord(letter)-97] += 1
            if counts[ord(letter)-97] == 2:
                return letter
        
        return -1
        