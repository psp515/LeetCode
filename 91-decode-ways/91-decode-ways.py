class Solution(object):
    def numDecodings(self, s):
        n = len(s)

        if s[0] == '0':
            return 0

        f = [0 for x in range(n + 1)]

        f[0] = 1
        f[1] = 0 if s[0] == "0" else 1

        for i in range(2, n + 1):

            if 0 < int(s[i - 1:i]) <= 9:
                f[i] += f[i - 1]

            if 10 <= int(s[i - 2:i]) <= 26:
                f[i] += f[i - 2]

        return f[len(s)]