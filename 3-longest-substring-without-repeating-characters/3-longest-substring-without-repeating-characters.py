class Solution(object):
    def lengthOfLongestSubstring(self, s):
        d = [0 for _ in range(256)]
        n = len(s)
        j = 0
        maxc = 0
        for i in range(n):
            letter = ord(s[i])
            d[letter] += 1
            if d[letter] == 2:
                while d[letter] == 2:
                    d[ord(s[j])] -= 1
                    j+=1
            maxc = max(maxc, i-j+1)
        
        return maxc