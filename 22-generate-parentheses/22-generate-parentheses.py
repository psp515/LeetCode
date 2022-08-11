class Solution(object):
    def _validate(self, s):
        open = 0

        for element in s:
            if element == "(":
                open += 1
            else:
                if open == 0:
                    return False

                open -= 1

        return True if open == 0 else False

    def _generate_all(self, max_len, data, arr):

        if len(data) == max_len:
            if self._validate(data):
                arr.append(data)
            return

        self._generate_all(max_len, data + ")", arr)
        self._generate_all(max_len, data + "(", arr)

    def generateParenthesis(self, n):
        combinations = []
        self._generate_all(n*2, "", combinations)
        return combinations
        
        