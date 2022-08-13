class Solution(object):

    def sort(self, word):
        new_word = ""

        arr = [0 for _ in range(26)]

        for letter in word:
            arr[ord(letter) - 97] += 1

        return arr

    def isAnagram(self, s, t):
        sorted_s = self.sort(s)
        sorted_t = self.sort(t)

        for i in range(26):
            if sorted_s[i] != sorted_t[i]:
                return False

        return True
        