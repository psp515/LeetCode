class Solution(object):
    def frequencySort(self, s):
        f = [[0, chr(i)] for i in range(256)]
        sorted = ""
        
        for letter in s:
            f[ord(letter)][0] += 1
        
        f.sort(key=lambda x:x[0], reverse=True)
        
        for i in range(256):
            if f[i] != 0:  
                sorted += f[i][0] * f[i][1]
        
        return sorted