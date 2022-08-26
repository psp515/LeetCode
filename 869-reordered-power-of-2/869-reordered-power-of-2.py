class Solution(object):
    def get_numbers(self, n):
        counts = [0 for _ in range(10)]
        while n:
            digit = n % 10
            n //= 10
            counts[digit] += 1
        
        return counts
    
    def cmp(self, a, b):
        
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        
        return True
    
    def lens(self, n):
        return int(math.log10(n)) + 1
    
    def reorderedPowerOf2(self, n):
        length = self.lens(n)
        
        n_digs = self.get_numbers(n)
        
        value = 1
        while self.lens(value) <= length:
            val_digs = self.get_numbers(value)
            
            if self.cmp(val_digs, n_digs):
                return True
            
            value *= 2
        
        return False