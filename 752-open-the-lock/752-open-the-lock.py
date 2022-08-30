class Solution(object):
    def shortest_path(self, G, target):
        path_len = -1 
        
        stack = []
    
    def openLock(self, deadends, target):
        if '0000' in deadends:
            return -1
        if '0000' == target:
            return 0
        
        stack = deque([('0000', 0)])
        visited = set(['0000'])
        
        while stack:
            x, d = stack.popleft()
            
            if x in deadends:
                continue
            if x == target:
                return d
            
            for i in range(4):
                num = int(x[i])
                
                for dx in [-1, 1]:
                    nx = x[:i] + str((num + dx) % 10) + x[i+1:]
                    if nx not in visited:
                        stack.append((nx, d + 1))
                        visited.add(nx)
                        
        return -1
        
        