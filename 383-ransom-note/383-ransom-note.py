class Solution(object):
    def sort(self, word):
        new_word = ""

        arr = [0 for _ in range(26)]

        for letter in word:
            arr[ord(letter) - 97] += 1

        return arr
    
    def canConstruct(self, ransomNote, magazine):
        if len(magazine) < len(ransomNote):
            return False
        
        magazine_letters = self.sort(magazine)
        
        for letter in ransomNote:
            index = ord(letter)-97
            if magazine_letters[index] > 0:
                magazine_letters[index] -= 1
            else:
                return False
            
        return True
        