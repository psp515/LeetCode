class MyQueue(object):

    def __init__(self):
        self.count = 0
        self.i = 0
        self.j = 0
        self.stack = [0 for _ in range(100)]

    def push(self, x):
        if self.count == 100:
            return
        
        self.stack[self.j] = x
        
        self.count += 1
        self.j = (self.j + 1) % 100
        

    def pop(self):
        if self.j == self.i:
            return None
        
        
        x = self.stack[self.i]
        self.i += 1
        self.count -= 1
        
        return x
        

    def peek(self):
        if self.count == 0:
            return None
        
        return self.stack[self.i]
        

    def empty(self):
        if self.count != 0:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()