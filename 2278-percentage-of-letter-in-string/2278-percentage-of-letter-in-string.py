class Solution(object):
    def percentageLetter(self, s, letter):
        count = 0
        for l in s:
            if l == letter:
                count+=1
                
        return (100*count)//len(s)
        