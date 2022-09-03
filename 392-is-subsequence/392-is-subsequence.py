class Solution(object):
    def isSubsequence(self, s, t):
        if s == "":
            return True
        n = len(t)
        for i in range(n):
            if t[i] == s[0]:
                indexer = 1
                if indexer == len(s):
                    return True
                
                for j in range(i+1, n):
                    if t[j] == s[indexer]:
                        indexer += 1
                    if indexer == len(s):
                        return True
        
        return False
        