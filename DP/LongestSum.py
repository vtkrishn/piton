a = [-2,-3,4,-1,-2,1,5,-3]
b = [-2,-3,-4,-1,-2,-1,-5,-3]

def mixedArray(a):
    maxSoFar = -1000
    maxEndingHere = 0
    for i in a:
        maxEndingHere = maxEndingHere + i
        if maxEndingHere < 0:    
            maxEndingHere = 0
        else:
            maxSoFar = max(maxSoFar,maxEndingHere)
    print maxSoFar

def allNegativeArray(b):
    maxSoFar = -1000
    maxEndingHere = 0
    for i in b:
        maxEndingHere = maxEndingHere + i
        maxSoFar = max(maxSoFar,maxEndingHere)
        maxSoFar = max(maxSoFar,i)
    print maxSoFar

mixedArray(a)
allNegativeArray(b)
