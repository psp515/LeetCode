class Solution(object):
    def fizzBuzz(self, n):
        f = []
        for i in range(1, n+1):
            if i % 15 == 0:
                f.append("FizzBuzz")
            elif i % 3 == 0:
                f.append("Fizz")
            elif i % 5 == 0:
                f.append("Buzz")
            else:
                f.append(str(i))
                
        return f