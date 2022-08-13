class Solution(object):
    def sort(self, word):
        new_word = ""

        arr = [0 for _ in range(26)]

        for letter in word:
            arr[ord(letter) - 97] += 1

        return arr
    
    def check(self, arr1, arr2):
        for i in range(26):
            if arr1[i] != arr2[i]:
                return False

        return True
    
    def checkInclusion(self, p, s):
        if len(p) > len(s):
            return False
        
        sorted_p = self.sort(p)

        if len(p) == len(s):
            if self.check(self.sort(s), sorted_p):
                return True
            return False

        sorted_s = self.sort(s[:len(p)])
        
        j = 0
        
        for i in range(len(p), len(s)):
            if self.check(sorted_s, sorted_p):
                return True

            sorted_s[ord(s[j]) - 97] -= 1
            j += 1
            sorted_s[ord(s[i]) - 97] += 1
        
        if self.check(sorted_s, sorted_p):
                return True
        
        return False
        