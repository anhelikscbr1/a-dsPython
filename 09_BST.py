
class BSTNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None

    def insert(self, value, node = None):
        if not self.root:
            self.root = BSTNode(value)
            return
        if(node.value > value):
            if(node.left):
                self.insert(value, node.left)
            else:
                node.left = BSTNode(value)
                return
        if node.value <= value:
            if(node.right):
                self.insert(value, node.right)
            else:
                node.right = BSTNode(value)
                return
    
    def inOrderTraversal(self, rootNode):
        if not rootNode: return
        self.inOrderTraversal(rootNode.left)
        print(rootNode.value)
        self.inOrderTraversal(rootNode.right)
    
    def searchNode(self, value, rootNode):
        if not rootNode: return 
        if(rootNode.value > value):
            self.searchNode(value, rootNode.left)
        elif(rootNode.value < value):
            self.searchNode(value, rootNode.right)
        else:
            return True
        return False

    def minVal(self, node):
        while(node.left):
            node = node.left    
        return node

    def deleteNode(self, node, value):
        if(node == None):
            return None
        if(node.value > value):
            node.left = self.deleteNode(node.left, value)
        elif(node.value < value):
            node.right = self.deleteNode(node.right, value)
        else: 
            if(not node.left):
                temp = node.right
                node = None
                return temp

            if(not node.right):
                temp = node.left
                node = None
                return temp
            
            minVal = self.minVal(node.right)
            node.value = minVal.value
            node.right = self.deleteNode(node.right, minVal.value)
        return node


myBST = BST()

myBST.insert(100)
myBST.insert(150, myBST.root)
myBST.insert(90, myBST.root)
myBST.insert(80, myBST.root)
myBST.insert(10, myBST.root)

myBST.inOrderTraversal(myBST.root)
print(
'-----------------------'
)

myBST.deleteNode(myBST.root, 100)
myBST.inOrderTraversal(myBST.root)