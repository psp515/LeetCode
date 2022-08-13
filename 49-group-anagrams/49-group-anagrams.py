class Solution(object):

    def sort(self, word):
        new_word = ""

        arr = [0 for i in range(26)]

        for letter in word:
            arr[ord(letter)-97] += 1

        for i in range(26):
            while arr[i] != 0:
                new_word += chr(i+97)
                arr[i] -= 1

        return new_word

    def groupAnagrams(self, arr):
        arr = [(self.sort(x), x) for x in arr]

        arr = sorted(arr)

        returnable = [[arr[0][1]]]
        n = len(arr)
        j = 0
        for i in range(1, n):
            if arr[i][0] == arr[i - 1][0]:
                returnable[j].append(arr[i][1])
            else:
                j += 1
                returnable.append([arr[i][1]])

        return returnable
        
        