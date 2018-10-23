import math
src = 1033
dest = 1069
list = [1033, 1039, 1049, 1051, 1061, 1063]

def isPrime(num):
    if num <= 3:
        return True
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True
    
# for i in range(src,dest):
#     if isPrime(i):
#         list.append(i)

    
print list
queue = []
visited = [0] * len(list)

queue.append(src)
visited[list.index(src)] = 1

while queue:
    s = queue.pop(0)
    def getClosest(src,list):
        result = []
        for i in list:
            k = int(int(i)-int(src))
            if  k < 10 or k % 10 == 0:
                if i != src:
                    result.append(i)
        return result    
        
    close = getClosest(src, list)
    
    for i in close:
        if not visited[list.index(i)]:
            visited[list.index(i)] = 1
            queue.append(i)
        if src == dest:
            return visited[]
print visited            

    