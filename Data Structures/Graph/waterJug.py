import math
class pair:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
def bfs(x, y, target):
    map = {}
    q = []
    q.append(pair(x,y))    
    while q:
        s = q.pop(0)
        p = pair(s.x,s.y)
        h = abs(hash(p))
        if map.has_key(h):
            continue
        
        if s.x > x or s.y > y or s.x < 0 or s.y < 0:
            continue
        
        q.append(p)
        
        map[h] = 1
        
        if s.x == target or s.y == target:
            if s.x == target:
                if s.y != 0:
                    q.append(pair(s.x,0))
            else:
                if s.x != 0:
                    q.append(pair(0,s.y))
        
        q.append(pair(s.x,x))
        q.append(pair(x,s.y))
        
        m=0
        if x > y:
            m=x
        else:
            m=y
        for i in range(m):
            c = s.x + i
            d = s.y - i
            if c == x or (d == 0 and d >= 0):
                q.append(pair(c,d))
            
            c = s.x - i
            d = s.y + i
            
            if d == y or (c == 0 and c >= 0):
                q.append(pair(c,d))
        
        q.append(pair(x,0))
        q.append(pair(0,y))
        

jug1 = 4
jug2 = 3
target = 2
bfs(jug1,jug2, target)