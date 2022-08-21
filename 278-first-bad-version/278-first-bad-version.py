# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        s, e = 0, n - 1
        last_bad = n
        while s <= e:
            q = (s+e) // 2
            
            if isBadVersion(q) == True:
                last_bad = q
                e = q - 1
            else:
                s = q + 1
        
        return last_bad
        