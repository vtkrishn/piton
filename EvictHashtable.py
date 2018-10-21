import time
import threading

class Node:
    def __init__(self,data,ttl):
        self.data = data
        self.ttl = ttl
        self.next = None
        
class HashTable:
    def __init__(self, capacity):
        self.size = capacity
        self.array = [None]*self.size
    
    def get(self,key):
        index = self.hashcode(key)
        item = self.array[index]
        #while not item.next:
        return item
    
    def hashcode(self,key):
        return hash(key) % self.size
    
    def put(self, key, value, ttl):
        node = Node(value,ttl)
        self.register(node)
        index = self.hashcode(key)
        if self.array[index]:
            item = self.array[index]
            self.array[index] = item
            while not item:
                item = item.next
            item.next = node
        else:
            self.array[index] = node
    
    def register(self, node):
        print Timer()
    
h = HashTable(4)
h.put('one',2,3)
h.put('two',4,3)
h.put('three',7,3)
h.put('four',17,3)
h.put('thr',8,3)
print h.get('four').data

