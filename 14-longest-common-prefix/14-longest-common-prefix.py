class Solution(object):
    def _commonLetter(self, arr, index):
        letter = arr[0][index]
        
        for i in range(1, len(arr)):
            if letter != arr[i][index]:
                return ""
            
        return letter 
    
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        prefix = ""
        
        shortest = len(min(strs, key = len))
        i = 0
        
        while i < shortest:
            letter = self._commonLetter(strs, i)
            
            if letter == "":
                break
                
            prefix += letter
            i+=1
                
        return prefix
        
        
        