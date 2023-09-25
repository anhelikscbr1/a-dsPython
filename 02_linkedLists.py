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

    def __str__(self):
        pos = self.head
        myPrint = ""
        while(pos):
            myPrint+= str(pos.value) + "->"
            pos = pos.nextNode
        myPrint += "None"
        return myPrint

    def append(self, value):
        new_node = Node(value);
        self.tail.nextNode = new_node
        self.tail = new_node
        self.length+=1
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.nextNode = self.head
        self.head = new_node
        self.length+=1

    def insert(self, value, index):
        if(index > self.length):
            print("The LS has no such index")
            return
        if(index == 0):
            self.prepend(value)
            return
        pos = self.head
        i = 0 
        while(True):            
            if(i == index - 1):
                new_node = Node(value)
                new_node.nextNode = pos.nextNode
                pos.nextNode = new_node
                self.length +=1
                return
            pos = pos.nextNode
            i+=1
        


myLS = LinkedList(1)
myLS.append(2)
myLS.append(4)
myLS.prepend(0)

myLS.insert(3, 3)
print(myLS.length)
print(myLS)