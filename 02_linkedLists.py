#* Singly linked lists

class Node:
    def __init__(self, value = 0):
        self.nextNode =  None
        self.value =  value

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node 
        self.length = 1
    
    def append(self, value):
        new_node = Node(value);
        self.tail.nextNode = new_node
        self.tail = new_node
        self.length+=1

    def printLinkedList(self):
        pos = self.head
        while(pos):
            print(pos.value)
            pos = pos.nextNode

myLS = LinkedList(1)
myLS.append(2)
myLS.append(3)
myLS.printLinkedList()
