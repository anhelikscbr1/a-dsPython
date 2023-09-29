
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

myBST = BST()

myBST.insert(100)
myBST.insert(150, myBST.root)
myBST.insert(90, myBST.root)
myBST.insert(80, myBST.root)

myBST.inOrderTraversal(myBST.root)

print(myBST.searchNode(150, myBST.root))