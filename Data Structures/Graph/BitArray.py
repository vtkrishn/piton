def checkCount(a,i,j,map,prev):
    if j >= len(a):
        if not map.has_key(prev):
            map[prev] = 1
        return
    if not map.has_key(prev):
        map[prev] = 1
    if not map.has_key(a[j]):
        map[a[j]] = 1
    checkCount(a,i,j+1, map,prev | a[j])

def count(a):
    map = {}
    for i in range(len(a)):
        if not map.has_key(a[i]):
            map[a[i]] = 1
            prev = 0
            checkCount(a,i,i+1, map,prev | a[i])
    
    print len(map)

count([1,2,4])