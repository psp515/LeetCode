class Solution(object):
    def get_sign(self, arr):
        z = 1
        for x in arr:
            if x < 0:
                z *= -1
        return z

    def get_len(self, start, end, direct, arr):
        z = self.get_sign(arr)
        if z > 0:
            return len(arr)

        for i in range(start, end, direct):
            if arr[i] < 0:
                z *= -1
                if direct == 1:
                    return abs(end - i - 1)
                else:
                    return abs(end - i + 1)

        return 0

    def getMaxLen(self, nums):
        subarrs = []
        add_arr = []
        for x in nums:
            if x == 0:
                if len(add_arr) != 0:
                    subarrs.append(add_arr)
                    add_arr = []
                continue

            add_arr.append(x)

        if len(add_arr) != 0:
            subarrs.append(add_arr)

        maxlen = 0

        for subar in subarrs:
            x = self.get_len(0, len(subar), 1, subar)
            y = self.get_len(len(subar) - 1, -1, -1, subar)
            maxlen = max(maxlen, x, y)

        return maxlen
            
        
        