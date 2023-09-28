
# * n element -> n-1 element -> ... -> last-element-added -> None
# ?Stack operations push, pop, peek, deleteStack, is empty

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class customStack:
    def __init__(self):
        self.head = None
    
    def printStack(self):
        aux = self.head
        if (self.isEmpty()):
            print('No values in the stack')
            return
        while(aux):
            print(aux.value)
            aux = aux.next

    def isEmpty(self):
        if(self.head == None):
            return True
        else: 
            return False

    def push(self,value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
    
    def pop(self):
        if(self.isEmpty()):
            return "The stack is empty"
        value = self.head.value
        self.head = self.head.next
        return str(value)

    def deleteStack(self):
        self.head = None



cs = customStack()
print(cs.isEmpty())
cs.push(0)
cs.push(1)
cs.push(2)
cs.printStack()
print(cs.pop() + " Has been deleted")
print(cs.pop() + " Has been deleted")
cs.printStack()
cs.deleteStack()
cs.printStack()
