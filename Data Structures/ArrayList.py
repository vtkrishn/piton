class ArrayList:
    
    def __init__(self,size):
        self.size = size
        self.list = []
    
    def add(self,a):
        if len(self.list) < self.size:
            self.list.append(a)
        else:
            self.doubleSize(self.size)
    
    def doubleSize(self,size):
        self.size = 2 * size
        tempList = (self.list) + [0]*(self.size)
        self.list = tempList    
        
    def insert(self, index, a):
        self.list.insert(index, a)
    
    def remove(self,a):
        if a in self.list:
            self.list.remove(a)
        else:
            print 'item not there'
    
    def iter(self):
        return (i for i in self.list)
    
a = ArrayList(5)

a.add(1)
a.add(4)
a.add(5)
a.remove(7)
a.add(7)
a.add(8)
a.add(9)

i = a.iter()