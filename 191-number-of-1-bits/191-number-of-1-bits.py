class Solution(object):
    def hammingWeight(self, n):
        counter = 0
        for x in bin(n):
            if x == '1':
                counter +=1
        return counter 
        