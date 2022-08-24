from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [False for _ in range(n)]
        visited[0] = True
        q = deque()
        
        q.append(0)
        
        while q:
            x = q.popleft()
            
            for z in rooms[x]:
                if not visited[z]:
                    visited[z] = True
                    q.append(z)  
        
        for x in visited:
            if not x:
                return False
        
        return True
        