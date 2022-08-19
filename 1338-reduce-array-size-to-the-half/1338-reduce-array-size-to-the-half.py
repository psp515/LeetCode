class Solution(object):
    def minSetSize(self, arr):
        n = len(arr)
        d = {}
        
        for element in arr:
            if element in d:
                d[element] += 1
            else:
                d[element] = 1
        
        data = list(d.items())
        
        data.sort(key = lambda x:x[1], reverse = True)
        
        selected = 0
        counter = 0
        while selected < n // 2:
            selected += data[counter][1]
            counter += 1
        
        return counter
        