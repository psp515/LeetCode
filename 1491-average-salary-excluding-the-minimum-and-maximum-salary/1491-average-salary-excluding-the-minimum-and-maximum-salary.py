class Solution(object):
    def average(self, salary):
        return float((float(sum(salary) - max(salary) - min(salary))) / (len(salary)-2))
        