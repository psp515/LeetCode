class Solution(object):
    def has_end(self, word, list):
        for x in list:
            if word == x:
                return True

        return False

    def ladderLength(self, beginWord, endWord, wordList):

        if not self.has_end(endWord, wordList):
            return 0

        stack = deque([(beginWord, 1)])
        d = {}
        d[beginWord] = 1
        wordSet = set(wordList)

        while stack:
            word, c = stack.popleft()
            if word == endWord:
                return c

            for i in range(len(word)):
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = word[:i] + letter + word[i+1:]
                    if tmp not in d and tmp in wordSet:
                        stack.append((tmp, c+1))
                        d[tmp] = True
        
        return 0