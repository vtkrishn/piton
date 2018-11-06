import random
#Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None
#linked list        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.map = []
    #add node
    def addNode(self,data):
        n = Node(data)
        self.map.append(n)
        if self.head:
            n.next = self.head
            self.head = n
        else:
            self.head = n
            self.tail = n
        
    #set the random node
    def setRandom(self):
        curr = self.head
        item = [0,1,2,3,4]
        random.shuffle(item)
        while curr is not None:
            index = random.choice(item)
            curr.random = self.map[index]
            curr = curr.next
    
    def printList(self,head):
        curr = head
        while curr is not None:
            print curr.data, '---->',curr.random.data
            curr = curr.next
            
    #clone the linked list
    def clone(self):
        curr = self.head
        while curr is not None:
            n = Node(str(str(curr.data) + 'Q'))
            print 'n-----',n.data, '---->',n.random
            nextNode = curr.next
            curr.next = n
            n.next = nextNode
            curr = nextNode
        
        curr = self.head
        tempHead = None
        while curr is not None and curr.next is not None:
            print '-----',curr.data, '---->',curr.random.data
            nextNode = curr.next
            #set new head
            if tempHead is None:
                tempHead = nextNode
            #clone random node
            nextNode.random = curr.random.next
            #wire next for orignal
            curr.next = nextNode.next
            print '-----',nextNode.data, '---->',nextNode.random.data
            #wire next for new clone
            nextNode.next = nextNode.next.next
            
            #move
            curr = curr.next
        
        
        
        return tempHead
            

#setup code    
l = LinkedList()
l.addNode(1)
l.addNode(2)
l.addNode(3)
l.addNode(4)
l.addNode(5)
l.setRandom()
l.printList(l.head)
print '----'
#clone code
l.printList(l.clone())
