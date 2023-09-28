
#? Operations: isEmpty, Enqueue, Dequeue, Peek, deleteQueue

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class customQueue():
    def __init__(self):
        self.head = None
        self.tail = None

    def printQueue(self):
        if(self.isEmpty()):
            print('THE QUEUE IS EMPTY')
            return
        pos = self.head
        while(pos):
            print(pos.value)
            pos = pos.next
    
    def isEmpty(self):
        if(self.head  == None and self.tail == None):
            return True

    def enQueue(self, value):
        newNode = Node(value)
        if(self.isEmpty()):
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode

    def deQueue(self):
        if(self.isEmpty()):
            return "The queue is alredy empty"
        value = str(self.head.value)
        if(self.head == self.tail):
            self.head = None
            self.tail = None
            return value + " Removed"
        self.head = self.head.next
        return value + " Removed"

myQueue = customQueue()
print(myQueue.deQueue())
myQueue.enQueue(1)
print(myQueue.deQueue())
myQueue.printQueue()
myQueue.enQueue(2)
myQueue.enQueue(3)
print(myQueue.deQueue())
print(myQueue.deQueue())
myQueue.enQueue(4)
myQueue.enQueue(5)
myQueue.enQueue(6)
print(myQueue.deQueue())

myQueue.printQueue()